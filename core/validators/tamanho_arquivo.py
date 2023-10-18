from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_tamanho_arquivo(value):
    tamanho = value.size
    if not tamanho < 4*1024*1024:
        raise ValidationError("O tamanho máximo do arquivo que pode ser carregado é de 4MB")
    