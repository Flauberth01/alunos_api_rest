from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_documentacao import AlunoDocumentacao


class TestAlunoDocumentacaoView(APITestCase):
    
    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04',
            email='joao@example.com',
            celular1='+55 123456789',
            celular2='+55 987654321',
            religiao='Cristã',
            ocupacao='Estudante',
            estado_civil='SOLTEIRO'
        )
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")
        self.documentacao = AlunoDocumentacao.objects.create(
            aluno=self.aluno,
            foto=foto_arquivo,
            comprovante_endereco=comprovante_arquivo,
            rg='123456789',
            orgao_emissor='SSP',
            data_expedicao='2000-02-15',
            cpf='98765432101',
            registro_alistamento='123456789012',
            cartao_sus='987654321012345',
            certidao_nova='12345678901234567890123456789012',
            tipo_certidao='CASAMENTO'
        )
        self.usuario = get_user_model().objects.create_user(
            username='teste',
            password='teste',
        )
        self.url = reverse('aluno_documentacao', kwargs={'aluno_id': self.documentacao.aluno.id})
        self.client.force_authenticate(self.usuario)

    def test_ler_documentacao_de_aluno_e_retornar_status_200(self):
        
        # when
        response = self.client.get(self.url)

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rg'], self.documentacao.rg)
        self.assertEqual(response.data['orgao_emissor'], self.documentacao.orgao_emissor)
        self.assertEqual(response.data['data_expedicao'], self.documentacao.data_expedicao)
        self.assertEqual(response.data['cpf'], self.documentacao.cpf)
        self.assertEqual(response.data['registro_alistamento'], self.documentacao.registro_alistamento)
        self.assertEqual(response.data['cartao_sus'], self.documentacao.cartao_sus)
        self.assertEqual(response.data['certidao_nova'], self.documentacao.certidao_nova)
        self.assertEqual(response.data['tipo_certidao'], self.documentacao.tipo_certidao)

    def test_ler_documentacao_de_aluno_inexistente_e_retornar_status_404(self):
        
        # when
        url = reverse('aluno_documentacao', kwargs={'aluno_id': 10})
        response = self.client.get(url)

        # then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_atualizar_documentacao_de_aluno(self):
        
        foto_arquivo = SimpleUploadedFile("foto2.jpg", b"foto2", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante2.pdf", b"comprovante2", content_type="application/pdf")
        
        # given
        dados_documentacao_do_aluno_novos = {
            'aluno': self.aluno.id,
            'foto': foto_arquivo,
            'comprovante_endereco': comprovante_arquivo,
            'rg': '123456789',
            'orgao_emissor': 'SSP',
            'data_expedicao': '2000-12-12',
            'cpf': '68635451015',
            'registro_alistamento': '012345678912',
            'cartao_sus': '123456789012345',
            'certidao_nova': '29347101552020147043047789291131',
            'tipo_certidao': 'NASCIMENTO'
        }

        # when
        response = self.client.put(self.url, data=dados_documentacao_do_aluno_novos, format='multipart')

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rg'], dados_documentacao_do_aluno_novos['rg'])
        self.assertEqual(response.data['orgao_emissor'], dados_documentacao_do_aluno_novos['orgao_emissor'])
        self.assertEqual(response.data['data_expedicao'], dados_documentacao_do_aluno_novos['data_expedicao'])
        self.assertEqual(response.data['cpf'], dados_documentacao_do_aluno_novos['cpf'])
        self.assertEqual(response.data['registro_alistamento'], dados_documentacao_do_aluno_novos['registro_alistamento'])
        self.assertEqual(response.data['cartao_sus'], dados_documentacao_do_aluno_novos['cartao_sus'])
        self.assertEqual(response.data['certidao_nova'], dados_documentacao_do_aluno_novos['certidao_nova'])
        self.assertEqual(response.data['tipo_certidao'], dados_documentacao_do_aluno_novos['tipo_certidao'])
        self.assertTrue(response.data['foto'])
        self.assertTrue(response.data['comprovante_endereco'])

    def test_atualizar_parcialmente_documentacao_de_aluno(self):
        
        # given
        dados_documentacao_do_aluno_novos = {
            'passaporte': '12345678'
        }

        # when
        response = self.client.patch(self.url, data=dados_documentacao_do_aluno_novos, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['passaporte'], dados_documentacao_do_aluno_novos['passaporte'])
        
    def test_atualizar_documentacao_de_aluno_com_dados_invalidos_e_retornar_status_400(self):
        
        # given
        dados_documentacao_do_aluno_novos = {
            'cpf': '31231312'
        }

        # when
        response = self.client.patch(self.url, data=dados_documentacao_do_aluno_novos, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)