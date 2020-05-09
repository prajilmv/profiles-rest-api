from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_alpha(value):
    for char in value:
        if char.isalpha():
            continue
        else:
            raise ValidationError(_('%(value)s contains non alphabetical charectors'),params={'value': value},)
            break;
