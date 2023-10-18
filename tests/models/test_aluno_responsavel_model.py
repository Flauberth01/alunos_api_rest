from django.forms import ValidationError
from django.test import TestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_responsavel import AlunoResponsavel


class AlunoResponsavelModelTests(TestCase):
    """Testes para o model de responsável do aluno"""

    def setUp(self):
        """Criação de um aluno para testes"""

        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04'
        )

    def test_criar_responsavel_do_aluno(self):
        """Teste de criação de responsável de aluno com todos os campos"""

        # given
        dados_responsavel_do_aluno = {
            'nome': 'Maria',
            'cpf': '08522804087',
            'responsavel_designado': True,
            'celular1': '62999999999',
            'celular2': '62988888888',
            'email': 'maria@gmail.com',
            'escolaridade': 'FUNDAMENTAL_CO',
            'filiacao1': False,
            'filiacao2': False,
            'parentesco': 'TIO'
        }

        # when
        aluno_responsavel = AlunoResponsavel(**dados_responsavel_do_aluno)
        aluno_responsavel.full_clean()
        aluno_responsavel.save()
        aluno_responsavel.aluno.add(self.aluno)

        # then
        self.assertIsNotNone(aluno_responsavel.id)
        self.assertIsNotNone(aluno_responsavel.aluno)
        
    def test_criar_responsavel_sem_campos_obrigatorios(self):
        """Teste de criação de responsável sem indicar o nome, um campo obrigatório"""

        # given
        dados_responsavel_do_aluno = {
            # Campo obrigatório nome não fornecido
            'cpf': '12345678901',
            'responsavel_designado': True,
            'celular1': '62999999999',
            'celular2': '62988888888',
            'email': 'maria@gmail.com',
            'escolaridade': 'FUNDAMENTAL_CO',
            'filiacao1': False,
            'filiacao2': False,
            'parentesco': 'TIO'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_responsavel = AlunoResponsavel(**dados_responsavel_do_aluno)
            aluno_responsavel.full_clean()
        
    def test_criar_responsavel_com_cpf_invalido(self):
        """Teste de criação de responsável indicando um cpf inválido"""

        # given
        dados_responsavel_do_aluno = {
            'nome': 'Maria',
            'cpf': '12345678912',   # CPF inválido
            'responsavel_designado': True,
            'celular1': '62999999999',
            'celular2': '62988888888',
            'email': 'maria@gmail.com',
            'escolaridade': 'FUNDAMENTAL_CO',
            'filiacao1': False,
            'filiacao2': False,
            'parentesco': 'TIO'
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_responsavel = AlunoResponsavel(**dados_responsavel_do_aluno)
            aluno_responsavel.full_clean()