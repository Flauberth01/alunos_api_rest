from django.db import models

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.choices.tipo_sanguineo import TipoSanguineo


class AlunoSaude(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='saude')
    tipo_sanguineo = models.CharField(max_length=11, choices=TipoSanguineo.choices, null=True, blank=True)
    problema_de_saude = models.TextField(max_length=300, null=True, blank=True)
    tratamento_com_medicacao = models.TextField(max_length=300, null=True, blank=True)
    medico_responsavel = models.CharField(max_length=50, null=True, blank=True)
    alergia_medicamento = models.TextField(max_length=300, null=True, blank=True)
    alergia_alimentar = models.TextField(max_length=300, null=True, blank=True)
    escolarizacao_domicilio = models.BooleanField(null=True, blank=True, default=False)
    escolarizacao_hospital = models.BooleanField(null=True, blank=True, default=False)
    acompanhamento_fonoaudiologo = models.BooleanField(null=True, blank=True, default=False)
    acompanhamento_psicologo = models.BooleanField(null=True, blank=True, default=False)
    acompanhamento_apae = models.BooleanField(null=True, blank=True, default=False)
    # TRANSTORNOS NEUROLÓGICOS
    tem_tdah = models.BooleanField(null=True, blank=True, default=False)
    tem_autismo = models.BooleanField(null=True, blank=True, default=False)
    tem_dislexia = models.BooleanField(null=True, blank=True, default=False)
    tem_dispraxia = models.BooleanField(null=True, blank=True, default=False)
    tem_superdotacao = models.BooleanField(null=True, blank=True, default=False)
    outro_transtorno_neuro = models.CharField(max_length=50, null=True, blank=True)
    # TRANSTORNOS MENTAIS
    tem_ansiedade = models.BooleanField(null=True, blank=True, default=False)
    tem_esquizofrenia = models.BooleanField(null=True, blank=True, default=False)
    tem_depressao = models.BooleanField(null=True, blank=True, default=False)
    tem_sindrome_do_panico = models.BooleanField(null=True, blank=True, default=False)
    tem_transtorno_bipolar = models.BooleanField(null=True, blank=True, default=False)
    outro_transtorno_mental = models.CharField(max_length=50, null=True, blank=True)
    # DEFICIÊNCIAS
    tem_baixa_visao = models.BooleanField(null=True, blank=True, default=False)
    tem_cegueira = models.BooleanField(null=True, blank=True, default=False)
    tem_impedimento_fala = models.BooleanField(null=True, blank=True, default=False)
    tem_surdez = models.BooleanField(null=True, blank=True, default=False)
    tem_deficiencia_auditiva = models.BooleanField(null=True, blank=True, default=False)
    tem_deficiencia_fisica = models.BooleanField(null=True, blank=True, default=False)
    tem_deficiencia_intelectual = models.BooleanField(null=True, blank=True, default=False)
    tem_deficiencia_multipla = models.BooleanField(null=True, blank=True, default=False)
      
    class Meta:
        db_table = 'aluno_saude'
        ordering = ['-id']
        verbose_name = 'Dados de saúde de aluno'
        verbose_name_plural = 'Dados de sáude de alunos'
    
    def __str__(self):
        return self.aluno.nome
