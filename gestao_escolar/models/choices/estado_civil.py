from django.db import models
from django.utils.translation import gettext_lazy as _


class EstadoCivil(models.TextChoices):
    SOLTEIRO = 'SOLTEIRO', _('Solteiro')
    CASADO = "CASADO", _("Casado")
    SEPARADO = 'SEPARADO', _('Separado')
    DIVORCIADO = 'DIVORCIADO', _('Divorciado')
    VIUVO = 'VIUVO', _('Viúvo')
    UNIAO_ESTAVEL = 'UNIAO_ESTAVEL', _('União estável')
