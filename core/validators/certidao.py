from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from validate_docbr import Certidao


def validate_certidao(value):
    if not Certidao().validate(value):
        raise ValidationError(
            _("%(value)s não é um número de certidão válido."),
            params={"value": value},
        )
