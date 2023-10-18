from django.db import models
from django.utils.translation import gettext_lazy as _


class TransporteRodoviario(models.TextChoices):
    BICICLETA = 'BICICLETA', _('Bicicleta')
    TRACAO_ANIMAL = "TRACAO_ANIMAL", _("Tração animal")
    ONIBUS = 'ONIBUS', _('Ônibus')
    MICRO_ONIBUS = 'MICRO_ONIBUS', _('Micro ônibus')
    VAN_KOMBI = 'VAN_KOMBI', _('Van ou Kombi')
    OUTRO = 'OUTRO', _('Outro')
    
    
class TransporteAquaviario(models.TextChoices):
    BARCO_5_ALUNOS = 'BARCO_5_ALUNOS', _('Embarcação para até 5 alunos')
    BARCO_15_ALUNOS = "BARCO_15_ALUNOS", _("Embarcação para até 15 alunos")
    BARCO_35_ALUNOS = 'BARCO_35_ALUNOS', _('Embarcação para até 35 alunos')
    BARCO_MAIS_DE_35 = 'BARCO_MAIS_DE_35', _('Embarcação para mais de 35 alunos')
