from django.db import models
from django.utils.translation import gettext_lazy as _


class Genero(models.TextChoices):
    MASCULINO = 'MASCULINO', _('Masculino')
    FEMININO = 'FEMININO', _('Feminino')
    NAO_BINARIO = 'NAO_BINARIO', _('Não-binário')
