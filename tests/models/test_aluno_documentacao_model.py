import os
from django.forms import ValidationError
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_documentacao import AlunoDocumentacao


class AlunoDocumentacaoModelTests(TestCase):
    """Testes para o modelo de documentação do aluno"""

    def setUp(self):
        """Criação de um aluno para testes"""

        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04'
        )

    def test_criar_aluno_documentacao(self):
        """Teste de criação de documentação de aluno com todos os campos preenchidos"""

        # Criar arquivos simulados para os campos de arquivo (foto e comprovante_endereco)
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")

        # given
        dados_documentacao_do_aluno = {
            'aluno': self.aluno,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'rne': '987654321',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12',
            'data_entrada_no_pais': '2002-03-02',
            'cpf': '68635451015',
            'nis': '73569286080',
            'registro_alistamento': '012345678912',
            'cartao_sus': '123456789012345',
            'id_educacenso': '123456789012',
            'certidao_nova': '29347101552020147043047789291131',
            'cert_antiga_livro': '123456',
            'cert_antiga_folha': '789',
            'cert_antiga_termo': '0123456',
            'tipo_certidao': 'NASCIMENTO',
            'passaporte': 'ABC12345',
        }

        # when
        aluno_documentacao = AlunoDocumentacao(**dados_documentacao_do_aluno)
        aluno_documentacao.full_clean()
        aluno_documentacao.save()

        # then
        self.assertIsNotNone(aluno_documentacao.id)
        
    def test_criar_aluno_documentacao_com_cpf_invalido(self):
        """Teste de criação de documentação de aluno com campo cpf inválido"""

        # Criar arquivos simulados para os campos de arquivo (foto e comprovante_endereco)
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")

        # given
        dados_documentacao_do_aluno = {
            'aluno': self.aluno,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12',
            'cpf': '123'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_documentacao = AlunoDocumentacao(**dados_documentacao_do_aluno)
            aluno_documentacao.full_clean()
            
    def test_criar_aluno_documentacao_com_nis_invalido(self):
        """Teste de criação de documentação de aluno com campo nis inválido"""

        # Criar arquivos simulados para os campos de arquivo (foto e comprovante_endereco)
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")

        # given
        dados_documentacao_do_aluno = {
            'aluno': self.aluno,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12',
            'nis': '123'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_documentacao = AlunoDocumentacao(**dados_documentacao_do_aluno)
            aluno_documentacao.full_clean()
    
    def test_criar_aluno_documentacao_com_certidao_invalida(self):
        """Teste de criação de documentação de aluno com campo certidão de modelo novo inválido"""

        # Criar arquivos simulados para os campos de arquivo (foto e comprovante_endereco)
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")

        # given
        dados_documentacao_do_aluno = {
            'aluno': self.aluno,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12',
            'certidao_nova': '123'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_documentacao = AlunoDocumentacao(**dados_documentacao_do_aluno)
            aluno_documentacao.full_clean()
            
    def test_criar_aluno_documentacao_com_formato_comprovante_invalido(self):
        """Teste de criação de documentação de aluno com campo comprovante de endereço recebendo um arquivo de formato inválido"""

        # Criar arquivos simulados para os campos de arquivo (foto e comprovante_endereco)
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("musica.mp3", b"musica", content_type="audio/mpeg")

        # given
        dados_documentacao_do_aluno = {
            'aluno': self.aluno,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_documentacao = AlunoDocumentacao(**dados_documentacao_do_aluno)
            aluno_documentacao.full_clean()
            
    def test_criar_aluno_documentacao_com_foto_arquivo_muito_grande(self):
        """Teste de criação de documentação de aluno com campo foto recebendo um arquivo muito grande"""

        conteudo_foto = os.urandom(51200000)
        # Criar arquivos simulados para os campos de arquivo (foto e comprovante_endereco)
        foto_arquivo = SimpleUploadedFile("foto.jpg", conteudo_foto, content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")

        # given
        dados_documentacao_do_aluno = {
            'aluno': self.aluno,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_documentacao = AlunoDocumentacao(**dados_documentacao_do_aluno)
            aluno_documentacao.full_clean()