from django.db import models
from django.utils.translation import gettext_lazy as _


class TipoSanguineo(models.TextChoices):
    A_POSITIVO = 'A_POSITIVO', _('A Positivo')
    A_NEGATIVO = 'A_NEGATIVO', _('A Negativo')
    B_POSITIVO = 'B_POSITIVO', _('B Positivo')
    B_NEGATIVO = 'B_NEGATIVO', _('B Negativo')
    AB_POSITIVO = 'AB_POSITIVO', _('AB Positivo')
    AB_NEGATIVO = 'AB_NEGATIVO', _('AB Negativo')
    O_POSITIVO = 'O_POSITIVO', _('O Positivo')
    O_NEGATIVO = 'O_NEGATIVO', _('O Negativo')
