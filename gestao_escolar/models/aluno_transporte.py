from django.db import models

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.choices.poder_publico import PoderPublico
from gestao_escolar.models.choices.transporte import TransporteRodoviario, TransporteAquaviario


class AlunoTransporte(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='transporte')
    utiliza_transporte_escolar = models.BooleanField()
    poder_responsavel = models.CharField(max_length=9, choices=PoderPublico.choices, null=True, blank=True)
    cadeirante = models.BooleanField(null=True, blank=True, default=False)
    area_de_risco = models.BooleanField(null=True, blank=True, default=False)
    transporte_rodoviario = models.CharField(max_length=13, choices=TransporteRodoviario.choices, null=True, blank=True)
    transporte_aquaviario = models.CharField(max_length=16, choices=TransporteAquaviario.choices, null=True, blank=True)
    
    class Meta:
        db_table = 'aluno_transporte'
        ordering = ['-id']
        verbose_name = 'Dados de transporte de aluno'
        verbose_name_plural = 'Dados de transporte de alunos'

    def __str__(self):
        return self.aluno.nome
