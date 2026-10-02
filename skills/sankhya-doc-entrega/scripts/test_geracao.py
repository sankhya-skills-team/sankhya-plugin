"""Auto-teste dos geradores. Executar: python scripts/test_geracao.py

Gera HTML e DOCX de exemplo em um diretorio temporario e verifica
versionamento, backup, historico e o preenchimento do modelo DS v.4.
Sem framework.
"""

import base64
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))

EXEMPLO = {
    "parceiro": "Parceiro Teste",
    "id_demanda": "DEM-0001",
    "nome_customizacao": "Pesagem de Entrada",
    "caminho_sistema": "Menu › Beneficiamento › BEN — Pesagem de Entrada",
    "responsavel_tecnico": "Dev A → Dev B (a partir da v1.1)",
    "email_responsavel": "dev.b@sankhya.com.br",
    "solicitante_sankhya": "Ana Paula Souza",
    "modulo_area": "Beneficiamento",
    "cidade": "Uberlândia",
    "objetivo": "Automatiza o registro de pesagem & libera a nota <fiscal>.",
    "limitacoes_gerais": ["Não reprocessa pesagens já encerradas."],
    "incluir_homologacao": True,
    "incluir_assinaturas": True,
    "funcionalidades": [{
        "titulo": "Calcular Pesagem",
        "tipo": "acao",
        "icone": "⚖️",
        "passos": ["O usuário seleciona o ticket.", "O sistema calcula o peso líquido."],
        "obs": "Requer perfil Balança.",
        "dicas": ["Confira a tara antes de calcular."],
        "limitacoes": "Irreversível após o encerramento.",
        "tipo_acesso": "tela",
        "testes": [
            {"nome": "Executar com ticket em aberto",
             "esperado": "Operação concluída — peso líquido gravado"},
            {"nome": "Executar com ticket encerrado",
             "esperado": 'Sistema bloqueia com mensagem: "Ticket já encerrado."'},
        ],
    }, {
        "titulo": "Encerrar Ticket",
        "tipo": "evento",
        "passos": ["O usuário confirma.", "O sistema encerra o ticket."],
    }],
    "checklist_deploy": {
        "pre_requisitos": [
            {"tipo": "tela_adicional", "nome": "AD_PESAGEM",
             "arquivo": "Metadados_AD_PESAGEM.zip", "observacao": ""},
            {"tipo": "parametro", "nome": "PESAGEM_TOL", "descricao": "Tolerância",
             "tipo_valor": "número", "valor_padrao": "0.5"},
        ],
        "pos_deploy": [
            {"tipo": "acao", "nome_exibicao": "Calcular Pesagem", "entidade": "AD_PESAGEM",
             "tipo_sankhya": "AcaoRotinaJava", "classe": "br.com.sankhya.X", "perfis": "Balança"},
            {"tipo": "jar", "arquivo": "pesagem-1.0.0.jar", "caminho_servidor": ""},
        ],
    },
}


# PNG 1x1 valido — o python-docx le o cabecalho da imagem ao embutir.
PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmM"
    "IQAAAABJRU5ErkJggg==")


def executar(script, dados, destino):
    dados = dict(dados, arquivo_saida=destino)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    entrada = os.path.join(os.path.dirname(destino), "_dados.json")
    with open(entrada, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False)
    # Sem Word: cada DOCX abriria o Office em segundo plano (~5 s). O caminho
    # com Word foi validado a mao; aqui se testa o fallback.
    return subprocess.run([sys.executable, os.path.join(AQUI, script), entrada],
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=dict(os.environ, DOC_ENTREGA_SEM_WORD="1"))


def gerar(script, dados, destino):
    saida = executar(script, dados, destino)
    assert saida.returncode == 0, "%s falhou:\n%s" % (script, saida.stderr)
    return json.loads(saida.stdout.strip().splitlines()[-1])


def com_evidencias(pasta):
    """Copia do EXEMPLO com uma evidencia no primeiro teste e outra no segundo."""
    os.makedirs(pasta, exist_ok=True)
    for nome in ("hom-fc1-1.png", "hom-fc1-2.png"):
        with open(os.path.join(pasta, nome), "wb") as f:
            f.write(PNG_1X1)
    func = dict(EXEMPLO["funcionalidades"][0])
    func["testes"] = [
        dict(EXEMPLO["funcionalidades"][0]["testes"][0], status="aprovado",
             evidencias=[{"arquivo": "hom-fc1-1.png",
                          "legenda": "Ticket 100% aberto & pesagem gravada."}]),
        dict(EXEMPLO["funcionalidades"][0]["testes"][1], status="reprovado",
             evidencias=[{"arquivo": "hom-fc1-2.png", "legenda": "Mensagem de bloqueio."}]),
    ]
    return dict(EXEMPLO, funcionalidades=[func])


def testar_html(tmp):
    alvo = os.path.join(tmp, "Documentacao", "Entrega - Pesagem de Entrada.html")
    r1 = gerar("gerar_html.py", EXEMPLO, alvo)
    assert r1["versao"] == "1.0" and r1["backup"] is None, r1
    html = open(alvo, encoding="utf-8").read()

    assert "&lt;fiscal&gt;" in html and "&amp;" in html, "escape HTML quebrado"
    assert "<svg" in html and "currentColor" in html, "logo SVG ausente"
    assert "#212F41" in html and "#00CD5E" in html, "paleta do Padrão 2026 ausente"
    assert "#4ADE80" not in html and "#243143" not in html, "cor antiga remanescente"
    assert html.count("data:image/jpeg;base64,") == 2, "fundo de capa/contracapa ausente"
    for trecho in ("Controle do", "01</span>Identificação", "08</span>Prazo de Garantia",
                   "Treinamento e Suporte", "Dúvidas? Fale com a gente."):
        assert trecho in html, "seção do modelo v.4 ausente: %s" % trecho
    assert "Líder do Projeto" in html and "Consultor" in html, "assinaturas padrão ausentes"
    assert "<td>Dev B</td>" in html, "autor do histórico errado"
    assert "congelarEstado" in html, "correção do export ausente"
    assert html.count("pesagem-1.0.0.jar") == 1, "nome do JAR repetido no detalhe"
    assert re.search(r'name="doc-versao" content="1\.0"', html)
    # nenhum placeholder de formatação sobrou no CSS
    assert "%(" not in html.split("<script>")[0], "placeholder %( no HTML/CSS"

    r2 = gerar("gerar_html.py", dict(EXEMPLO, changelog=["Ajuste de tolerância."]), alvo)
    assert r2["versao"] == "1.1", r2
    assert r2["backup"] and os.path.exists(r2["backup"]), "backup não criado"
    html2 = open(alvo, encoding="utf-8").read()
    assert "Ajuste de tolerância." in html2 and "v1.0" in html2, "histórico não acumulou"

    # Sem homologação a numeração segue corrida: Treinamento vira 05.
    sem_hom = os.path.join(tmp, "semhom", "Documentacao", "Entrega - X.html")
    gerar("gerar_html.py", dict(EXEMPLO, incluir_homologacao=False), sem_hom)
    html_sh = open(sem_hom, encoding="utf-8").read()
    assert "05</span>Treinamento" in html_sh and "Homologação e Testes" not in html_sh

    # Addon Studio: o tipo servico tem rotulo proprio
    addon = dict(EXEMPLO, funcionalidades=[
        dict(EXEMPLO["funcionalidades"][0], titulo="Processar Fechamento", tipo="servico")])
    alvo_ad = os.path.join(tmp, "addon", "Documentacao", "Entrega - Frete.html")
    gerar("gerar_html.py", addon, alvo_ad)
    assert "Serviço da Tela" in open(alvo_ad, encoding="utf-8").read(), "rótulo de @Service"


def testar_docx(tmp):
    from docx import Document

    alvo = os.path.join(tmp, "Documentacao", "Entrega - Pesagem de Entrada.docx")
    r3 = gerar("gerar_docx.py", EXEMPLO, alvo)
    assert r3["versao"] == "1.0", r3          # extensao diferente = versao propria
    r4 = gerar("gerar_docx.py", dict(EXEMPLO, changelog=["Revisão do escopo."]), alvo)
    assert r4["versao"] == "1.1" and os.path.exists(r4["backup"]), r4

    assert r4["sumario_atualizado"] is False, r4
    doc = Document(alvo)
    assert doc.core_properties.version == "1.1"
    # Sem Word para atualizar o sumario, o arquivo pede a atualizacao ao abrir.
    assert doc.settings.element.findall(qn_w("updateFields")), "fallback sem updateFields"
    texto = "\n".join(p.text for p in doc.paragraphs)
    celulas = [c.text for t in doc.tables for r in t.rows for c in r.cells]

    # Saiu do template DS v.4: capa, estilos e cabeçalho vêm do modelo.
    assert "Pesagem de Entrada" in texto and "< Nome do projeto >" not in texto, "capa"
    assert any(s.style_id == "SkCapaLinha1" for s in doc.styles), "estilos do modelo ausentes"
    cabecalho = "".join(t.text or "" for t in doc.sections[1].header._element.iter(qn_w("t")))
    assert "DELIVERY SERVICE TECH" in cabecalho.upper(), "cabeçalho do modelo perdido"
    for valor in ("Parceiro Teste", "DEM-0001", "Ana Paula Souza", "Beneficiamento",
                  "Dev B — dev.b@sankhya.com.br"):
        assert valor in celulas, "campo não preenchido: %s" % valor
    assert "Receitas por Categoria" not in texto, "exemplo do modelo sobrou"
    assert "O usuário seleciona o ticket." in texto
    assert "Confira a tara antes de calcular." in texto, "dicas de uso ausentes"
    assert "Uberlândia, < dia >" in texto, "cidade não preenchida"
    assert all(any(papel in c for c in celulas) for papel in ("Líder do Projeto", "Consultor")),         "assinaturas padrão"
    assert "Checklist de deploy" in texto, "checklist fora dos anexos"
    assert "Executar com ticket encerrado" in celulas, "tabela de cenários ausente"

    # Histórico: mais antiga primeiro, com o autor da versão.
    hist = next(t for t in doc.tables if t.rows[0].cells[0].text == "VERSÃO")
    assert [r.cells[0].text for r in hist.rows[1:]] == ["1.0", "1.1"], "ordem do histórico"
    assert hist.rows[2].cells[2].text == "Dev B", "autor da versão ausente"

    # Cada funcionalidade tem a propria instancia de lista numerada: sem isso
    # os passos da segunda continuariam a contagem da primeira.
    num_ids = {p._p.find(".//" + qn_w("numId")).get(qn_w("val"))
               for p in doc.paragraphs if p.text in ("O usuário seleciona o ticket.",
                                                     "O usuário confirma.")}
    assert len(num_ids) == 2, "passos sem reinício de numeração"

    # Sem homologação o capítulo 05 sai inteiro; sem assinaturas, a data também.
    alvo_sh = os.path.join(tmp, "semhom", "Documentacao", "Entrega - X.docx")
    gerar("gerar_docx.py", dict(EXEMPLO, incluir_homologacao=False,
                                incluir_assinaturas=False), alvo_sh)
    texto_sh = "\n".join(p.text for p in Document(alvo_sh).paragraphs)
    assert "Homologação e Testes" not in texto_sh and "< Cidade >" not in texto_sh


def qn_w(tag):
    from docx.oxml.ns import qn
    return qn("w:" + tag)


def testar_evidencias(tmp):
    from docx import Document

    base_ev = os.path.join(tmp, "ev")
    dados_ev = com_evidencias(os.path.join(base_ev, "Documentacao", "evidencias"))

    alvo_ev = os.path.join(base_ev, "Documentacao", "Entrega - Pesagem.html")
    gerar("gerar_html.py", dados_ev, alvo_ev)
    html_ev = open(alvo_ev, encoding="utf-8").read()
    assert html_ev.count('<div class="evidence-gallery">') == 2, "galeria não renderizada"
    assert html_ev.count("data:image/png;base64,") == 2, "imagem não embutida"
    assert "Ticket 100% aberto &amp; pesagem gravada." in html_ev, "legenda perdida"
    assert "status-btn aprovado" in html_ev and "status-btn reprovado" in html_ev, \
        "status do teste não aplicado"
    assert html_ev.count("1 imagem anexada") == 2, "contador de evidências errado"

    alvo_ev_dx = os.path.join(base_ev, "Documentacao", "Entrega - Pesagem.docx")
    gerar("gerar_docx.py", dados_ev, alvo_ev_dx)
    doc_ev = Document(alvo_ev_dx)
    texto_ev = "\n".join(p.text for p in doc_ev.paragraphs)
    assert "Capturas de tela" in texto_ev, "evidências fora dos anexos"
    assert "Evidência 01 — Ticket 100% aberto & pesagem gravada." in texto_ev
    assert "Evidência 02 — Mensagem de bloqueio." in texto_ev
    assert "< Capturas de tela >" not in texto_ev, "placeholder de anexos sobrou"
    # Logo da contracapa (inline do modelo) + 2 evidências.
    assert len(doc_ev.inline_shapes) == 3, "logo + 2 evidências esperados"
    resultados = [c.text for t in doc_ev.tables for r in t.rows for c in r.cells]
    assert any("(X) Aprovado" in c for c in resultados), "aprovação não marcada"
    assert any("(X) Reprovado" in c for c in resultados), "reprovação não marcada"

    # Evidencia ausente avisa, mas o documento sai — inclusive com as
    # evidencias que sobraram no mesmo teste.
    faltante = dict(dados_ev)
    faltante["funcionalidades"] = [dict(dados_ev["funcionalidades"][0])]
    faltante["funcionalidades"][0]["testes"] = [
        {"nome": "Cenário sem print", "esperado": "y",
         "evidencias": [{"arquivo": "nao-existe.png", "legenda": ""},
                        {"arquivo": "hom-fc1-1.png", "legenda": "A que existe."}]}]
    alvo_falta = os.path.join(base_ev, "Documentacao", "Entrega - Falta.html")
    saida = executar("gerar_html.py", faltante, alvo_falta)
    assert saida.returncode == 0, "evidência ausente derrubou a geração"
    assert "nao-existe.png" in saida.stderr, "falta não avisada no stderr"
    relatorio = json.loads(saida.stdout.strip().splitlines()[-1])
    assert [f["caso"] for f in relatorio["evidencias_faltando"]] == ["hom-fc1-1"], relatorio
    assert relatorio["evidencias_faltando"][0]["teste"] == "Cenário sem print"
    html_falta = open(alvo_falta, encoding="utf-8").read()
    assert html_falta.count("data:image/png;base64,") == 1, "evidência válida perdida"


def main():
    tmp = tempfile.mkdtemp(prefix="doc-entrega-")
    try:
        testar_html(tmp)
        testar_docx(tmp)
        testar_evidencias(tmp)
        print("OK — HTML e DOCX gerados, versionados e validados.")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
