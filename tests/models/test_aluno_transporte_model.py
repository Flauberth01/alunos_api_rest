from django.forms import ValidationError
from django.test import TestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_transporte import AlunoTransporte


class AlunoTransporteModelTestCase(TestCase):
    """Testes para o model de transporte do aluno"""

    def setUp(self):
        """Criação de um aluno para testes"""

        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04'
        )

    def test_criar_transporte_do_aluno(self):
        """Teste de criação de transporte do aluno com todos os campos"""

        # given
        dados_transporte_do_aluno = {
            'aluno': self.aluno,
            'utiliza_transporte_escolar': True,
            'poder_responsavel': 'ESTADUAL',
            'cadeirante': True,
            'area_de_risco': False,
            'transporte_rodoviario': 'ONIBUS',
            'transporte_aquaviario': ''
        }

        # when
        aluno_transporte = AlunoTransporte(**dados_transporte_do_aluno)
        aluno_transporte.full_clean()
        aluno_transporte.save()

        # then
        self.assertIsNotNone(aluno_transporte.id)
        
    def test_criar_transporte_do_aluno_sem_campos_obrigatórios(self):
        """Teste de criação de transporte sem indicar utilização de transporte escolar, um campo obrigatório"""

        # given
        dados_transporte_do_aluno = {
            'aluno': self.aluno,
            # Campo obrigatório utiliza_transporte_escolar não fornecido
            'poder_responsavel': 'ESTADUAL',
            'cadeirante': True,
            'area_de_risco': False,
            'transporte_rodoviario': 'ONIBUS',
            'transporte_aquaviario': ''
        }

        # when & then
        with self.assertRaises(ValidationError):
            aluno_transporte = AlunoTransporte(**dados_transporte_do_aluno)
            aluno_transporte.full_clean()