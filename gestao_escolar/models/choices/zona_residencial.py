from django.db import models
from django.utils.translation import gettext_lazy as _


class ZonaResidencial(models.TextChoices):
    URBANA = 'URBANA', _('Urbana')
    RURAL = 'RURAL', _('Rural')
