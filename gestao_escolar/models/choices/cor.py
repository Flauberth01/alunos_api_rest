from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoriaCor(models.TextChoices):
    PRETO = 'PRETO', _('Preto')
    PARDO = 'PARDO', _('Pardo')
    BRANCO = 'BRANCO', _('Branco')
    INDIGENA = 'INDIGENA', _('Indígena')
    AMARELO = 'AMARELO', _('Amarelo')
