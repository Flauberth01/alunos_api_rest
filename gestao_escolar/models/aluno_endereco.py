from django.db import models

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.choices.unidade_federativa import UnidadeFederativa
from gestao_escolar.models.choices.zona_residencial import ZonaResidencial


class AlunoEndereco(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='endereco')
    pais = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UnidadeFederativa.choices)
    municipio = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length=20)
    zona_residencial = models.CharField(max_length=10, choices=ZonaResidencial.choices)
    complemento = models.TextField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'aluno_endereco'
        ordering = ['-id']
        verbose_name = 'Endereço de aluno'
        verbose_name_plural = 'Endereços de alunos'

    def __str__(self):
        return f"Endereço de {self.aluno.nome}"
