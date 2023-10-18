from django.db import models

from gestao_escolar.models.aluno import Aluno


class AlunoAssistencia(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='assistencia')
    # RECURSOS AUXILIARES
    recurso_ledor = models.BooleanField(null=True, blank=True, default=False)
    recurso_transcricao = models.BooleanField(null=True, blank=True, default=False)
    recurso_interprete = models.BooleanField(null=True, blank=True, default=False)
    recurso_prova_fonte_18 = models.BooleanField(null=True, blank=True, default=False)
    recurso_prova_fonte_24 = models.BooleanField(null=True, blank=True, default=False)
    recurso_cd_com_audio = models.BooleanField(null=True, blank=True, default=False)
    recurso_material_braille = models.BooleanField(null=True, blank=True, default=False)
    # ATENDIMENTO EDUCACIONAL ESPECIALIZADO
    aee_funcoes_cognitivas = models.BooleanField(null=True, blank=True, default=False)
    aee_vida_autonoma = models.BooleanField(null=True, blank=True, default=False)
    aee_enriquecimento_curricular = models.BooleanField(null=True, blank=True, default=False)
    aee_libras = models.BooleanField(null=True, blank=True, default=False)
    aee_informatica_acessivel = models.BooleanField(null=True, blank=True, default=False)
    aee_portugues_segunda_lingua = models.BooleanField(null=True, blank=True, default=False)
    aee_calculo_soroban = models.BooleanField(null=True, blank=True, default=False)
    aee_braille = models.BooleanField(null=True, blank=True, default=False)
    aee_orientacao_e_mobile = models.BooleanField(null=True, blank=True, default=False)
    aee_comunicacao_alternativa = models.BooleanField(null=True, blank=True, default=False)
    aee_recursos_opticos = models.BooleanField(null=True, blank=True, default=False)
      
    class Meta:
        db_table = 'aluno_assistencia'
        ordering = ['-id']
        verbose_name = 'Recursos de assistência do aluno'
        verbose_name_plural = 'Recursos de assistência de alunos'

    def __str__(self):
        return self.aluno.nome
