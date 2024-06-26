from django.db import models
from django.utils.translation import gettext_lazy as _


class UnidadeFederativa(models.TextChoices):
    AC = 'AC', _('Acre')
    AL = 'AL', _('Alagoas')
    AP = 'AP', _('Amapá')
    AM = 'AM', _('Amazonas')
    BA = 'BA', _('Bahia')
    CE = 'CE', _('Ceará')
    DF = 'DF', _('Distrito Federal')
    ES = 'ES', _('Espírito Santo')
    GO = 'GO', _('Goiás')
    MA = 'MA', _('Maranhão')
    MT = 'MT', _('Mato Grosso')
    MS = 'MS', _('Mato Grosso do Sul')
    MG = 'MG', _('Minas Gerais')
    PA = 'PA', _('Pará')
    PB = 'PB', _('Paraíba')
    PR = 'PR', _('Paraná')
    PE = 'PE', _('Pernambuco')
    PI = 'PI', _('Piauí')
    RJ = 'RJ', _('Rio de Janeiro')
    RN = 'RN', _('Rio Grande do Norte')
    RS = 'RS', _('Rio Grande do Sul')
    RO = 'RO', _('Rondônia')
    RR = 'RR', _('Roraima')
    SC = 'SC', _('Santa Catarina')
    SP = 'SP', _('São Paulo')
    SE = 'SE', _('Sergipe')
    TO = 'TO', _('Tocantins')
