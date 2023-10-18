from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_endereco import AlunoEndereco


class AlunoEnderecoViewTestCase(APITestCase):

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
        self.endereco = AlunoEndereco.objects.create(
            aluno=self.aluno,
            pais='Brasil',
            uf='GO',
            municipio='Goiânia',
            cep='74785-010',
            bairro='Jardim Lajeado',
            logradouro='Rua JL',
            numero='10',
            zona_residencial='URBANA',
            complemento='Casa 01',
        )
        self.usuario = get_user_model().objects.create_user(
            username='teste',
            password='teste',
        )
        self.url = reverse('aluno_endereco', kwargs={'aluno_id': self.endereco.aluno.id})
        self.client.force_authenticate(self.usuario)

    def test_ler_endereco_de_aluno_e_retornar_status_200(self):
        
        # when
        response = self.client.get(self.url)

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pais'], self.endereco.pais)
        self.assertEqual(response.data['uf'], self.endereco.uf)
        self.assertEqual(response.data['municipio'], self.endereco.municipio)
        self.assertEqual(response.data['cep'], self.endereco.cep)
        self.assertEqual(response.data['bairro'], self.endereco.bairro)
        self.assertEqual(response.data['logradouro'], self.endereco.logradouro)
        self.assertEqual(response.data['numero'], self.endereco.numero)
        self.assertEqual(response.data['zona_residencial'], self.endereco.zona_residencial)
        self.assertEqual(response.data['complemento'], self.endereco.complemento)

    def test_ler_endereco_de_aluno_inexistente_e_retornar_status_404(self):
        
        # when
        url = reverse('aluno_endereco', kwargs={'aluno_id': 1000})
        response = self.client.get(url)

        # then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_atualizar_endereco_de_aluno(self):
        
        # given
        dados_endereco_do_aluno_novos = {
            'aluno': self.aluno.id,
            'pais': 'Brasil',
            'uf': 'GO',
            'municipio': 'Goiânia',
            'cep': '74785-011',
            'bairro': 'Jardim Lajeado',
            'logradouro': 'Rua JL',
            'numero': '11',
            'zona_residencial': 'URBANA',
            'complemento': 'Casa 02'
        }

        # when
        response = self.client.put(self.url, data=dados_endereco_do_aluno_novos, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pais'], dados_endereco_do_aluno_novos['pais'])
        self.assertEqual(response.data['uf'], dados_endereco_do_aluno_novos['uf'])
        self.assertEqual(response.data['municipio'], dados_endereco_do_aluno_novos['municipio'])
        self.assertEqual(response.data['cep'], dados_endereco_do_aluno_novos['cep'])
        self.assertEqual(response.data['bairro'], dados_endereco_do_aluno_novos['bairro'])
        self.assertEqual(response.data['logradouro'], dados_endereco_do_aluno_novos['logradouro'])
        self.assertEqual(response.data['numero'], dados_endereco_do_aluno_novos['numero'])
        self.assertEqual(response.data['zona_residencial'], dados_endereco_do_aluno_novos['zona_residencial'])
        self.assertEqual(response.data['complemento'], dados_endereco_do_aluno_novos['complemento'])

    def test_atualizar_parcialmente_endereco_de_aluno(self):
        
        # given
        dados_endereco_do_aluno_novos = {
            'municipio': 'Aparecida de Goiânia'
        }

        # when
        response = self.client.patch(self.url, data=dados_endereco_do_aluno_novos, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['municipio'], dados_endereco_do_aluno_novos['municipio'])
        
    def test_atualizar_endereco_de_aluno_sem_dados_obrigatorios_e_retornar_status_400(self):
        
        # given
        dados_endereco_do_aluno_novos = {
            'municipio': ''
        }

        # when
        response = self.client.patch(self.url, data=dados_endereco_do_aluno_novos, format='json')

        # then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
