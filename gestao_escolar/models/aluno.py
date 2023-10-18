from django.db import models

from gestao_escolar.models.choices.cor import CategoriaCor
from gestao_escolar.models.choices.estado_civil import EstadoCivil
from gestao_escolar.models.choices.genero import Genero


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    nome_social = models.CharField(max_length=50, null=True, blank=True)
    nacionalidade = models.CharField(max_length=30)
    cor = models.CharField(max_length=8, choices=CategoriaCor.choices)
    genero = models.CharField(max_length=11, choices=Genero.choices)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)
    religiao = models.CharField(max_length=30, null=True, blank=True)
    ocupacao = models.CharField(max_length=30, null=True, blank=True)
    estado_civil = models.CharField(max_length=13, choices=EstadoCivil.choices, null=True, blank=True)

    class Meta:
        db_table = 'aluno'
        ordering = ['-id']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome
