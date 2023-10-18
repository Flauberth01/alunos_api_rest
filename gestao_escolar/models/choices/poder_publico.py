from django.db import models
from django.utils.translation import gettext_lazy as _


class PoderPublico(models.TextChoices):
    MUNICIPAL = 'MUNICIPAL', _('Municipal')
    ESTADUAL = 'ESTADUAL', _('Estadual')
