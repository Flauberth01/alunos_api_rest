from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from validate_docbr import CPF


def validate_cpf(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(
            _('%(value)s não é um CPF válido'),
            params={'value': value},
        )
