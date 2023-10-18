from django.db import models
from django.utils.translation import gettext_lazy as _


class Parentesco(models.TextChoices):
    PROPRIO = 'PROPRIO', _('Próprio(a) aluno(a)')
    TIO = 'TIO', _('Tio(a)')
    AVO = 'AVO', _('Avô(ó)')
    IRMAO = 'IRMAO', _('Irmão(ã)')
    PADRASTO = 'PADRASTO', _('Padrato ou madrasta')
    OUTRO = 'OUTRO', _('Outro')
