from django.db import models

from core.validators.cpf import validate_cpf
from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.choices.escolaridade import Escolaridade
from gestao_escolar.models.choices.parentesco import Parentesco


class AlunoResponsavel(models.Model):
    aluno = models.ManyToManyField(Aluno, related_name='responsaveis')
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, validators=[validate_cpf])
    responsavel_designado = models.BooleanField()
    celular1 = models.CharField(max_length=14)
    celular2 = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    escolaridade = models.CharField(max_length=14, choices=Escolaridade.choices, null=True, blank=True)
    filiacao1 = models.BooleanField(null=True, blank=True)
    filiacao2 = models.BooleanField(null=True, blank=True)
    parentesco = models.CharField(max_length=14, choices=Parentesco.choices, null=True, blank=True)

    class Meta:
        db_table = 'aluno_responsavel'
        ordering = ['-id']
        verbose_name = 'Pai/Responsável de aluno'
        verbose_name_plural = 'Pais/Reponsáveis de alunos'

    def __str__(self):
        return self.nome
