from django.db import models
from django.utils.translation import gettext_lazy as _


class TipoCertidao(models.TextChoices):
    NASCIMENTO = 'NASCIMENTO', _('Nascimento')
    CASAMENTO = 'CASAMENTO', _('Casamento')
