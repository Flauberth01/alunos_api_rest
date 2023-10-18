from django.test import TestCase

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_assistencia import AlunoAssistencia

class AlunoAssistenciaModelTests(TestCase):
    """Testes para o model de assistência do aluno"""

    def setUp(self):
        """Criação de um aluno para testes"""

        self.aluno = Aluno.objects.create(
            nome='João',
            nacionalidade='Brasil',
            cor='BRANCO',
            genero='MASCULINO',
            data_nascimento='2023-10-04'
        )

    def test_criar_assistencia_do_aluno(self):
        """Teste de criação de assistência de aluno com todos os campos"""

        # given
        dados_assistencia_do_aluno = {
            'aluno': self.aluno,
            'recurso_ledor': True,
            'recurso_transcricao': False,
            'recurso_interprete': True,
            'recurso_prova_fonte_18': False,
            'recurso_prova_fonte_24': False,
            'recurso_cd_com_audio': False,
            'recurso_material_braille': True,
            'aee_funcoes_cognitivas': False,
            'aee_vida_autonoma': False,
            'aee_enriquecimento_curricular': False,
            'aee_libras': True,
            'aee_informatica_acessivel': False,
            'aee_portugues_segunda_lingua': False,
            'aee_calculo_soroban': False,
            'aee_braille': True,
            'aee_orientacao_e_mobile': False,
            'aee_comunicacao_alternativa': False,
            'aee_recursos_opticos': False
        }

        # when
        aluno_assistencia = AlunoAssistencia(**dados_assistencia_do_aluno)
        aluno_assistencia.full_clean()
        aluno_assistencia.save()

        # then
        self.assertIsNotNone(aluno_assistencia.id)