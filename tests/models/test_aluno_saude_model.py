from django.test import TestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_saude import AlunoSaude


class AlunoSaudeModelTests(TestCase):
    """Testes para o model de saúde do aluno"""

    def setUp(self):
        """Criação de um aluno para testes"""

        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04'
        )

    def test_criar_saude_do_aluno(self):
        """Teste de criação de saúde de aluno com todos os campos"""

        # given
        dados_saude_do_aluno = {
            'aluno': self.aluno,
            'tipo_sanguineo': 'A_POSITIVO',
            'problema_de_saude': 'Asma',
            'tratamento_com_medicacao': 'Inalador',
            'medico_responsavel': 'Dr. José',
            'alergia_medicamento': 'Penicilina',
            'alergia_alimentar': 'Amendoim',
            'escolarizacao_domicilio': True,
            'escolarizacao_hospital': False,
            'acompanhamento_fonoaudiologo': True,
            'acompanhamento_psicologo': False,
            'acompanhamento_apae': False,
            'tem_tdah': False,
            'tem_autismo': False,
            'tem_dislexia': False,
            'tem_dispraxia': False,
            'tem_superdotacao': False,
            'outro_transtorno_neuro': None,
            'tem_ansiedade': False,
            'tem_esquizofrenia': False,
            'tem_depressao': False,
            'tem_sindrome_do_panico': False,
            'tem_transtorno_bipolar': False,
            'outro_transtorno_mental': None,
            'tem_baixa_visao': False,
            'tem_cegueira': False,
            'tem_impedimento_fala': False,
            'tem_surdez': False,
            'tem_deficiencia_auditiva': False,
            'tem_deficiencia_fisica': False,
            'tem_deficiencia_intelectual': False,
            'tem_deficiencia_multipla': False
        }

        # when
        aluno_saude = AlunoSaude(**dados_saude_do_aluno)
        aluno_saude.full_clean()
        aluno_saude.save()

        # then
        self.assertIsNotNone(aluno_saude.id)