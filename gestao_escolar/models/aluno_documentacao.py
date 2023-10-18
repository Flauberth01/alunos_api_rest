from django.db import models

from core.validators.tamanho_arquivo import validate_tamanho_arquivo
from core.validators.extensao_arquivo import validate_extensao_arquivo, validate_extensao_imagem
from core.validators.cpf import validate_cpf
from core.validators.nis import validate_nis
from core.validators.certidao import validate_certidao
from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.choices.tipo_certidao import TipoCertidao


def diretorio_de_arquivos_do_aluno(instance, filename):
    return f'gestao_escolar/aluno/{instance.aluno.nome}_{instance.aluno.id}/arquivos/{filename}'


class AlunoDocumentacao(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='documentacao')
    foto = models.FileField(upload_to=diretorio_de_arquivos_do_aluno, null=True, blank=True, validators=[validate_extensao_imagem,
                                                                                                          validate_tamanho_arquivo])
    comprovante_endereco = models.FileField(upload_to=diretorio_de_arquivos_do_aluno, null=True, blank=True, validators=[validate_extensao_arquivo, 
                                                                                                                         validate_tamanho_arquivo])
    rg = models.CharField(max_length=9, null=True, blank=True)
    rne = models.CharField(max_length=9, null=True, blank=True)
    orgao_emissor = models.CharField(max_length=8, null=True, blank=True)
    data_expedicao = models.DateField(null=True, blank=True)
    data_entrada_no_pais = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True, validators=[validate_cpf])
    nis = models.CharField(max_length=11, unique=True, null=True, blank=True, validators=[validate_nis])
    registro_alistamento = models.CharField(max_length=12, unique=True, null=True, blank=True)
    cartao_sus = models.CharField(max_length=15, unique=True, null=True, blank=True)
    id_educacenso = models.CharField(max_length=12, unique=True, null=True, blank=True)
    certidao_nova = models.CharField(max_length=32, unique=True, null=True, blank=True, validators=[validate_certidao])
    cert_antiga_livro = models.CharField(max_length=6, null=False, blank=True)
    cert_antiga_folha = models.CharField(max_length=3, null=False, blank=True)
    cert_antiga_termo = models.CharField(max_length=7, null=False, blank=True)
    tipo_certidao = models.CharField(max_length=10, choices=TipoCertidao.choices, null=True, blank=True)
    passaporte = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        db_table = 'aluno_documentacao'
        ordering = ['-id']
        verbose_name = 'Documentação de aluno'
        verbose_name_plural = 'Documentações de alunos'

    def __str__(self):
        return self.aluno.nome
