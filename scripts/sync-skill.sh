#!/usr/bin/env bash
#
# sync-skill.sh — sincroniza uma skill entre o repositório fonte público
# (github.com/ratk/skill-<nome>) e este plugin, via git subtree.
#
# As skills deste plugin são mantidas como subtree; a fonte da verdade são os
# repositórios individuais. Use este script para propagar mudanças nos dois sentidos.
#
#   pull  = traz a evolução do repositório fonte para o plugin
#   push  = devolve ao repositório fonte o que foi alterado aqui no plugin
#
# Uso:
#   scripts/sync-skill.sh <nome-skill> <pull|push> [branch]
#
# Exemplos:
#   scripts/sync-skill.sh sankhya-addon pull
#   scripts/sync-skill.sh sankhya-jape  pull master     # jape usa branch master
#   scripts/sync-skill.sh sankhya-bi    push
#
# Observações:
# - branch padrão: main (sankhya-jape usa master).
# - push exige acesso de escrita ao repositório fonte (mantenedor).
# - Os AGENTES (agents/) NÃO são subtree: foram adicionados por cópia.
#   Para atualizá-los, copie os arquivos do repositório ratk/sankhya-agents.
#
set -euo pipefail

NOME="${1:-}"
OP="${2:-}"
BRANCH="${3:-main}"

if [[ -z "$NOME" || -z "$OP" ]]; then
  echo "uso: scripts/sync-skill.sh <nome-skill> <pull|push> [branch]" >&2
  exit 2
fi

REPO="https://github.com/ratk/skill-${NOME}.git"
PREFIX="skills/${NOME}"

# roda a partir da raiz do repositório do plugin
cd "$(git rev-parse --show-toplevel)"

if [[ ! -d "$PREFIX" ]]; then
  echo "erro: '$PREFIX' não existe — a skill '$NOME' não está montada como subtree." >&2
  exit 1
fi

case "$OP" in
  pull)
    echo ">> subtree pull  $PREFIX  <-  $REPO@$BRANCH"
    git subtree pull --prefix="$PREFIX" "$REPO" "$BRANCH" --squash
    ;;
  push)
    echo ">> subtree push  $PREFIX  ->  $REPO@$BRANCH"
    git subtree push --prefix="$PREFIX" "$REPO" "$BRANCH"
    ;;
  *)
    echo "operação inválida: '$OP' (use pull ou push)" >&2
    exit 2
    ;;
esac
