from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from validate_docbr import PIS


def validate_nis(value):
    nis = PIS()
    if not nis.validate(value):
        raise ValidationError(
            _('%(value)s não é um NIS válido'),
            params={'value': value},
        )
