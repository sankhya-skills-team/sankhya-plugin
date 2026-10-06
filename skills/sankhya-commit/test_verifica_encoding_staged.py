#!/usr/bin/env python3
"""Testes de verifica_encoding_staged.py. Executar: python -m unittest test_verifica_encoding_staged"""
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import verifica_encoding_staged as v

TEXTO_ACENTUADO = 'ação de validação\n'
EDITORCONFIG_JAVA_LATIN1_KOTLIN_UTF8 = (
    'root = true\n'
    '[**/Java/src/**]\ncharset = latin1\n'
    '[**/Kotlin/src/**]\ncharset = utf-8\n'
)


class RepositorioTemporario:
    """Repositório git descartável com helpers para gravar e colocar arquivos no stage."""

    def __init__(self):
        self._diretorio = tempfile.TemporaryDirectory()
        self.raiz = self._diretorio.name
        self._git('init', '-q')
        self._git('config', 'user.name', 'Teste')
        self._git('config', 'user.email', 'teste@teste.com')
        self._git('config', 'core.autocrlf', 'false')

    def _git(self, *args):
        subprocess.run(['git', '-C', self.raiz] + list(args), check=True, capture_output=True)

    def gravar(self, caminho, conteudo):
        destino = os.path.join(self.raiz, caminho)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, 'wb') as arquivo:
            arquivo.write(conteudo)

    def stage(self, caminho, conteudo):
        self.gravar(caminho, conteudo)
        self._git('add', '--', caminho)

    def commitar(self):
        self._git('commit', '-q', '-m', 'base')

    def limpar(self):
        self._diretorio.cleanup()


class TesteBase(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioTemporario()
        self.addCleanup(self.repo.limpar)

    def achados(self):
        return v.verificar_staged(self.repo.raiz)

    def severidades(self, caminho):
        return [a.severidade for a in self.achados() if a.caminho == caminho]


class TesteCamadaCaractere(TesteBase):
    def test_caractere_substituicao_e_erro(self):
        self.repo.stage('a/Teste.java', b'// a\xef\xbf\xbd\xef\xbf\xbdo\n')
        self.assertIn(v.ERRO, self.severidades('a/Teste.java'))

    def test_encodings_misturados_e_erro(self):
        conteudo = TEXTO_ACENTUADO.encode('utf-8') + TEXTO_ACENTUADO.encode('latin-1')
        self.repo.stage('web/pagina.html', conteudo)
        self.assertEqual([v.ERRO], self.severidades('web/pagina.html'))

    def test_mojibake_em_utf8_e_aviso(self):
        self.repo.stage('web/pagina.html', 'aÃ§Ã£o\n'.encode('utf-8'))
        self.assertEqual([v.AVISO], self.severidades('web/pagina.html'))

    def test_mojibake_em_latin1_e_aviso(self):
        self.repo.stage('web/pagina.html', b'a\xc3\xa7\xc3\xa3o ' + 'ç'.encode('latin-1') + b'\n')
        self.assertIn(v.AVISO, self.severidades('web/pagina.html'))

    def test_html_latin1_sem_politica_nao_gera_achado(self):
        self.repo.stage('web/pagina.html', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([], self.achados())

    def test_binario_e_ignorado(self):
        self.repo.stage('lib/pacote.jar', b'PK\x00\x00\xef\xbf\xbd')
        self.repo.stage('lib/dados.txt', b'\x00\xef\xbf\xbd')
        self.assertEqual([], self.achados())

    def test_arquivo_ascii_nao_gera_achado(self):
        self.repo.stage('Java/src/Teste.java', b'class Teste {}\n')
        self.assertEqual([], self.achados())

    def test_nome_com_espaco_e_acento(self):
        self.repo.stage('Objetos de Banco/açao.txt', b'// a\xef\xbf\xbdo\n')
        self.assertEqual([v.ERRO], self.severidades('Objetos de Banco/açao.txt'))


class TestePoliticaPadrao(TesteBase):
    def test_java_latin1_ok(self):
        self.repo.stage('src/Teste.java', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([], self.achados())

    def test_java_utf8_e_erro(self):
        self.repo.stage('src/Teste.java', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertEqual([v.ERRO], self.severidades('src/Teste.java'))

    def test_kotlin_utf8_ok(self):
        self.repo.stage('src/Teste.kt', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertEqual([], self.achados())

    def test_kotlin_latin1_e_erro(self):
        self.repo.stage('src/Teste.kt', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([v.ERRO], self.severidades('src/Teste.kt'))

    def test_xml_em_pasta_sankhya_utf8_e_erro(self):
        self.repo.stage('datadictionary/Tabela.xml', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertEqual([v.ERRO], self.severidades('datadictionary/Tabela.xml'))

    def test_xml_fora_de_pasta_sankhya_nao_impoe(self):
        self.repo.stage('config/pom.xml', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertEqual([], self.achados())


class TestePoliticaEditorconfig(TesteBase):
    def test_editorconfig_latin1_com_arquivo_utf8_e_erro(self):
        self.repo.stage('.editorconfig', EDITORCONFIG_JAVA_LATIN1_KOTLIN_UTF8.encode('utf-8'))
        self.repo.stage('d/Java/src/Teste.java', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertEqual([v.ERRO], self.severidades('d/Java/src/Teste.java'))

    def test_editorconfig_kotlin_utf8_com_arquivo_latin1_e_erro(self):
        self.repo.stage('.editorconfig', EDITORCONFIG_JAVA_LATIN1_KOTLIN_UTF8.encode('utf-8'))
        self.repo.stage('d/Kotlin/src/Teste.kt', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([v.ERRO], self.severidades('d/Kotlin/src/Teste.kt'))

    def test_divergencia_em_tipo_nao_sankhya_e_aviso(self):
        self.repo.stage('.editorconfig', b'[*.sql]\ncharset = utf-8\n')
        self.repo.stage('banco/Campo.sql', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([v.AVISO], self.severidades('banco/Campo.sql'))

    def test_sem_charset_declarado_nao_impoe(self):
        self.repo.stage('.editorconfig', b'[*]\nindent_style = space\n')
        self.repo.stage('web/pagina.html', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([], self.achados())

    def test_ultima_secao_que_casa_vence(self):
        self.repo.stage('.editorconfig', b'[*.sql]\ncharset = utf-8\n[banco/*.sql]\ncharset = latin1\n')
        self.repo.stage('banco/Campo.sql', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([], self.achados())


class TesteOrigemDaPolitica(TesteBase):
    def mensagem(self, caminho):
        return [a.mensagem for a in self.achados() if a.caminho == caminho][0]

    def test_mensagem_indica_padrao_embutido_sem_editorconfig(self):
        self.repo.stage('src/Teste.java', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertIn('padrão embutido', self.mensagem('src/Teste.java'))

    def test_mensagem_indica_editorconfig_quando_declarado(self):
        self.repo.stage('.editorconfig', EDITORCONFIG_JAVA_LATIN1_KOTLIN_UTF8.encode('utf-8'))
        self.repo.stage('d/Java/src/Teste.java', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertIn('.editorconfig', self.mensagem('d/Java/src/Teste.java'))


class TesteComparacaoComHead(TesteBase):
    def test_mudanca_de_encoding_vs_head_e_aviso(self):
        self.repo.stage('web/pagina.html', TEXTO_ACENTUADO.encode('latin-1'))
        self.repo.commitar()
        self.repo.stage('web/pagina.html', TEXTO_ACENTUADO.encode('utf-8'))
        self.assertEqual([v.AVISO], self.severidades('web/pagina.html'))

    def test_mesmo_encoding_vs_head_nao_gera_achado(self):
        self.repo.stage('web/pagina.html', TEXTO_ACENTUADO.encode('latin-1'))
        self.repo.commitar()
        self.repo.stage('web/pagina.html', (TEXTO_ACENTUADO * 2).encode('latin-1'))
        self.assertEqual([], self.achados())


class TesteIndiceNaoDisco(TesteBase):
    def test_le_o_conteudo_do_indice_e_nao_do_disco(self):
        self.repo.stage('notas/Teste.txt', b'// a\xef\xbf\xbdo\n')
        self.repo.gravar('notas/Teste.txt', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual([v.ERRO], self.severidades('notas/Teste.txt'))

    def test_arquivo_removido_do_stage_nao_e_verificado(self):
        self.repo.stage('src/Teste.java', TEXTO_ACENTUADO.encode('latin-1'))
        self.repo.commitar()
        subprocess.run(['git', '-C', self.repo.raiz, 'rm', '-q', 'src/Teste.java'], check=True)
        self.assertEqual([], self.achados())


class TesteGlobEditorconfig(unittest.TestCase):
    def casa(self, glob, caminho):
        return bool(v.glob_para_regex(glob).match(caminho))

    def test_asteriscos_duplos_atravessam_pastas(self):
        self.assertTrue(self.casa('**/Java/src/**', 'demanda/Java/src/br/com/Teste.java'))

    def test_asterisco_simples_nao_atravessa_pastas(self):
        self.assertFalse(self.casa('banco/*.sql', 'banco/sub/Campo.sql'))

    def test_chaves_com_alternativas(self):
        self.assertTrue(self.casa('*.{java,kt}', 'a/b/Teste.kt'))
        self.assertFalse(self.casa('*.{java,kt}', 'a/b/Teste.xml'))

    def test_glob_sem_barra_vale_em_qualquer_pasta(self):
        self.assertTrue(self.casa('*.sql', 'a/b/Campo.sql'))


class TesteLinhaDeComando(TesteBase):
    def test_codigo_de_saida_1_quando_ha_erro(self):
        self.repo.stage('src/Teste.java', b'// a\xef\xbf\xbdo\n')
        self.assertEqual(1, v.principal(['--repo', self.repo.raiz]))

    def test_codigo_de_saida_0_quando_so_ha_aviso(self):
        self.repo.stage('web/pagina.html', 'aÃ§Ã£o\n'.encode('utf-8'))
        self.assertEqual(0, v.principal(['--repo', self.repo.raiz]))

    def test_codigo_de_saida_0_quando_limpo(self):
        self.repo.stage('src/Teste.java', TEXTO_ACENTUADO.encode('latin-1'))
        self.assertEqual(0, v.principal(['--repo', self.repo.raiz]))


if __name__ == '__main__':
    unittest.main()
