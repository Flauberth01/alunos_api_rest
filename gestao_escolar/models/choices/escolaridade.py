from django.db import models
from django.utils.translation import gettext_lazy as _

class Escolaridade(models.TextChoices):
    ANALFABETO = 'ANALFABETO', _('Analfabeto')
    FUNDAMENTAL_IN = 'FUNDAMENTAL_IN', _('Ensino Fundamental Incompleto')
    FUNDAMENTAL_CO = 'FUNDAMENTAL_CO', _('Ensino Fundamental Completo')
    MEDIO_IN = 'MEDIO_IN', _('Ensino Médio Incompleto')
    MEDIO_CO = 'MEDIO_CO', _('Ensino Médio Completo')
    SUPERIOR_IN = 'SUPERIOR_IN', _('Ensino Superior Incompleto')
    SUPERIOR_CO = 'SUPERIOR_CO', _('Ensino Superior Completo')
    POS_GRADUACAO = 'POS_GRADUACAO', _('Pós-Graduação Completa')
    MESTRADO = 'MESTRADO', _('Mestrado')
    DOUTORADO = 'DOUTORADO', _('Doutorado')
