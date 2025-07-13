from rest_framework.serializers import ValidationError
from server.form.constants import FORM_TEMPLATE_STATUS_CHOICES, ErrorCodes, ErrorMessages


def validate_form_template_status(value, allowed_statuses=FORM_TEMPLATE_STATUS_CHOICES):
  if (len(allowed_statuses) == 0 or
      not isinstance(allowed_statuses, list) or
      not all(isinstance(status, str) for status in allowed_statuses)):
    raise ValueError("allowed_statuses must be a non-empty list of strings")
  
  if value not in [status for status in allowed_statuses]:
    raise ValidationError({
      "code": ErrorCodes.FORM_TEMPLATE_STATUS_INVALID,
      "message": ErrorMessages.FORM_TEMPLATE_STATUS_INVALID,
      "field": "status"
    })
  return value