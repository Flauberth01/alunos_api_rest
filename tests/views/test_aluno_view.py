from django.contrib.auth import get_user_model
from django.http import QueryDict
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import encode_multipart
from rest_framework import status
from rest_framework.test import APITestCase

from gestao_escolar.models.aluno import Aluno


class AlunoViewSetTestCase(APITestCase):

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
        self.usuario = get_user_model().objects.create_user(
            username='teste',
            password='teste',
        )
        self.url = reverse('alunos-list')
        self.client.force_authenticate(self.usuario)

    def test_criar_aluno_e_retornar_status_201(self):
        """Teste de criação de aluno com todas as suas dependências"""
        
        foto_arquivo = SimpleUploadedFile("foto.jpg", b"foto", content_type="image/jpeg")
        comprovante_arquivo = SimpleUploadedFile("comprovante.pdf", b"comprovante", content_type="application/pdf")
        
        # given
        # given
        dados_documentacao = {
            "foto": foto_arquivo,
            "comprovante_endereco": comprovante_arquivo,
            "rg": "123456789",
            "orgao_emissor": "SSP",
            "data_expedicao": "2000-02-15",
            "cpf": "64999043092",
            "registro_alistamento": "123456789012",
            "cartao_sus": "123456789012345",
            "id_educacenso": "123456789012",
            "certidao_nova": "16067901552013109802046595243618",
            "tipo_certidao": "NASCIMENTO"
        }
        dados_aluno = {
            "documentacao": None,
            "endereco": {
                "pais": "Brasil",
                "uf": "SP",
                "municipio": "São Paulo",
                "cep": "12345678",
                "bairro": "Centro",
                "logradouro": "Rua Principal",
                "numero": "123",
                "zona_residencial": "URBANA",
                "complemento": "Apartamento 456"
            },
            "responsaveis": [
                {
                    "nome": "Seu João",
                    "cpf": "55991041091",
                    "responsavel_designado": True,
                    "celular1": "987654321",
                    "email": "paijoao@example.com",
                    "escolaridade": "SUPERIOR_CO",
                    "filiacao1": True,
                    "filiacao2": False,
                    "parentesco": None
                },
                {
                    "nome": "Dona João",
                    "cpf": "85452994009",
                    "responsavel_designado": False,
                    "celular1": "987654322",
                    "email": "maejoao@example.com",
                    "escolaridade": "MEDIO_CO",
                    "filiacao1": False,
                    "filiacao2": True,
                    "parentesco": None
                },
            ],
            "transporte": {
                "utiliza_transporte_escolar": True,
                "poder_responsavel": "ESTADUAL",
                "cadeirante": False,
                "area_de_risco": False,
                "transporte_rodoviario": "ONIBUS",
                "transporte_aquaviario": None
            },
            "nome": "João da Silva",
            "nome_social": "Joãozinho",
            "nacionalidade": "Brasileira",
            "cor": "BRANCO",
            "genero": "MASCULINO",
            "data_nascimento": "2000-01-01",
            "email": "joao@example.com",
            "celular1": "1234567890",
            "celular2": "1234567891",
            "religiao": "Católica",
            "ocupacao": "Estudante",
            "estado_civil": "SOLTEIRO"
        }
        # É NECESSÁRIO FAZER O ENCODING DE DADOS_DOCUMENTAÇAO COMO MULTIPART JÁ QUE ELE ENVIA ARQUIVOS
        # E O DO RESTANTE DE DADOS_ALUNO COMO JSON PORQUE MULTIPART NÃO PERMITE DADOS ANINHADOS
        dados_documentacao_encoded = encode_multipart(boundary=None, data=dados_documentacao)
        dados_documentacao_dict = QueryDict(dados_documentacao_encoded, encoding='utf-8').dict()
        dados_aluno["documentacao"] = dados_documentacao_dict

        # when
        response = self.client.post(self.url, data=dados_aluno, format='json')
        
        # then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_listar_alunos_e_retornar_status_200(self):
        """Teste de listagem de alunos"""
        
        # when
        response = self.client.get(self.url)

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Aluno.objects.count())
        
    def test_ler_aluno_e_retornar_status_200(self):
        """Teste de leitura de aluno"""

        # when
        url = reverse('alunos-detail', kwargs={'pk': self.aluno.pk})
        response = self.client.get(url)

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_aluno_e_retornar_status_200(self):
        """Teste de atualização de aluno"""
        
        # given
        aluno = Aluno.objects.first()
        url = reverse('alunos-detail', kwargs={'pk': aluno.pk})
        dados_aluno = {
            'nome': "João da Silva",
            "nome_social": "Joana",
            "nacionalidade": "Brasileiro",
            "cor": "BRANCO",
            "genero": "MASCULINO",
            "data_nascimento": "2000-01-15",
            "email": "joao.silva@example.com",
            "celular1": "(11) 98765-4321",
            "celular2": "(11) 12345-6789",
            "religiao": "Católico",
            "ocupacao": "Estudante",
            "estado_civil": "SOLTEIRO"
        }

        # when
        response = self.client.put(url, data=dados_aluno, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], dados_aluno['nome'])
        self.assertEqual(response.data['nome_social'], dados_aluno['nome_social'])
        self.assertEqual(response.data['nacionalidade'], dados_aluno['nacionalidade'])
        self.assertEqual(response.data['cor'], dados_aluno['cor'])
        self.assertEqual(response.data['genero'], dados_aluno['genero'])
        self.assertEqual(response.data['data_nascimento'], dados_aluno['data_nascimento'])
        self.assertEqual(response.data['email'], dados_aluno['email'])
        self.assertEqual(response.data['celular1'], dados_aluno['celular1'])
        self.assertEqual(response.data['celular2'], dados_aluno['celular2'])
        self.assertEqual(response.data['religiao'], dados_aluno['religiao'])
        self.assertEqual(response.data['ocupacao'], dados_aluno['ocupacao'])
        self.assertEqual(response.data['estado_civil'], dados_aluno['estado_civil'])

    def test_editar_parcialmente_aluno_e_retornar_status_200(self):
        """Teste de edição parcial de aluno"""
        
        # given
        aluno = Aluno.objects.first()
        url = reverse('alunos-detail', kwargs={'pk': aluno.pk})
        dados_aluno = {
            'nome': 'Beltrano',
            'nome_social': 'Sicrano'
        }

        # when
        response = self.client.patch(url, data=dados_aluno, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_aluno_e_retornar_status_204(self):
        """Teste de exclusão de aluno"""
        
        # given
        aluno = Aluno.objects.first()
        url = reverse('alunos-detail', kwargs={'pk': aluno.pk})

        # when
        response = self.client.delete(url)

        # then
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
