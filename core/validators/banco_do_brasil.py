from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_banco_do_brasil(value):
    if value != 'Banco do Brasil':
        raise ValidationError(
            _('O banco %(value)s não é permitido, apenas Banco do Brasil'),
            params={'value': value},
        )
