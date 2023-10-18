from django.forms import ValidationError
from django.test import TestCase

from gestao_escolar.models import Aluno


class AlunoModelTestCase(TestCase):
    """Testes para o model de aluno"""
    
    def test_criar_aluno_com_dados_obrigatorios(self):
        """Teste de criação de aluno apenas com os campos obrigatórios"""

        # given
        dados_aluno = {
            'nome': 'João',
            'nacionalidade': 'Brasil',
            'cor': 'BRANCO',
            'genero': 'MASCULINO',
            'data_nascimento': '2023-10-04'
        }

        # when
        aluno = Aluno(**dados_aluno)
        aluno.full_clean()
        aluno.save()

        # then
        self.assertIsNotNone(aluno.id)

    def test_criar_aluno(self):
        """Teste de criação de aluno com todos os campos"""

        # given
        dados_aluno = {
            'nome': 'João',
            'nome_social': 'Joãozinho',
            'nacionalidade': 'Brasil',
            'cor': 'BRANCO',
            'genero': 'MASCULINO',
            'data_nascimento': '2023-10-04',
            'email': 'joao@example.com',
            'celular1': '+55 123456789',
            'celular2': '+55 987654321',
            'religiao': 'Cristã',
            'ocupacao': 'Estudante',
            'estado_civil': 'SOLTEIRO',
        }

        # when
        aluno = Aluno(**dados_aluno)
        aluno.clean_fields()
        aluno.save()

        # then
        self.assertIsNotNone(aluno.id)
    
    def test_criar_aluno_sem_campos_obrigatorios(self):
        """Teste de criação de aluno sem indicar nome, um campo obrigatório"""

        # given
        dados_aluno = {
            # Campo obrigatório nome não fornecido
            'nome_social': 'Joãozinho',
            'nacionalidade': 'Brasil',
            'cor': 'BRANCO',
            'genero': 'MASCULINO',
            'data_nascimento': '2023-10-04',
            'email': 'joao@example.com',
            'celular1': '+55 123456789',
            'celular2': '+55 987654321',
            'religiao': 'Cristã',
            'ocupacao': 'Estudante',
            'estado_civil': 'SOLTEIRO',
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno = Aluno(**dados_aluno)
            aluno.full_clean()
