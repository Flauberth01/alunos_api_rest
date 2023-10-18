from django.forms import ValidationError
from django.test import TestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_endereco import AlunoEndereco


class AlunoEnderecoModelTests(TestCase):
    """Testes para o model de endereço do aluno"""

    def setUp(self):
        """Criação de um aluno para testes"""

        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04'
        )

    def test_criar_endereco_do_aluno(self):
        """Teste de criação de endereço de aluno com todos os campos"""

        # given
        dados_endereco_do_aluno = {
            'aluno': self.aluno,
            'pais': 'Brasil',
            'uf': 'GO',
            'municipio': 'Goiânia',
            'cep': '74785-010',
            'bairro': 'Jardim Lajeado',
            'logradouro': 'Rua JL',
            'numero': '10',
            'zona_residencial': 'URBANA',
            'complemento': 'Casa 01'
        }

        # when
        aluno_endereco = AlunoEndereco(**dados_endereco_do_aluno)
        aluno_endereco.full_clean()
        aluno_endereco.save()

        # then
        self.assertIsNotNone(aluno_endereco.id)
        
    def test_criar_endereco_sem_campos_obrigatorios(self):
        """Teste de criação de endereço sem indicar o país, um campo obrigatório"""

        # given
        dados_endereco_do_aluno = {
            'aluno': self.aluno,
            # O campo "pais" não foi fornecido, o que é obrigatório.
            'uf': 'GO',
            'municipio': 'Goiânia',
            'cep': '74785-010',
            'bairro': 'Jardim Lajeado',
            'logradouro': 'Rua JL',
            'numero': '10',
            'zona_residencial': 'URBANA',
            'complemento': 'Casa 01'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_endereco = AlunoEndereco(**dados_endereco_do_aluno)
            aluno_endereco.full_clean()
