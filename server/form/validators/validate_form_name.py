from form.models import FormTemplate, FormTemplateStatus
from form.constants import ErrorCodes, ErrorMessages
from rest_framework.serializers import ValidationError


def validate_form_name(value):
    if not value:
        raise ValidationError({
            "code": ErrorCodes.FORM_NAME_INVALID,
            "message": ErrorMessages.FORM_NAME_INVALID,
            "field": "name",
        })
    if len(value) > 255:
        raise ValidationError({
            "code": ErrorCodes.FORM_NAME_TOO_LONG,
            "message": ErrorMessages.FORM_NAME_TOO_LONG,
            "field": "name",
        })
    if len(value) < 3:
        raise ValidationError({
            "code": ErrorCodes.FORM_NAME_TOO_SHORT,
            "message": ErrorMessages.FORM_NAME_TOO_SHORT,
            "field": "name",
            "min_length": 3
        })
    return value
  