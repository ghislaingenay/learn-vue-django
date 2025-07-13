# form/constants.py
from django.utils.translation import gettext_lazy as _

class ErrorCodes:
    """Error codes for API responses"""
    
    # User-related errors
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_INVALID = "USER_INVALID"
    
    # Form template errors
    FORM_NAME_REQUIRED = "FORM_NAME_REQUIRED"
    FORM_NAME_TOO_SHORT = "FORM_NAME_TOO_SHORT"
    FORM_NAME_TOO_LONG = "FORM_NAME_TOO_LONG"
    FORM_NAME_INVALID = "FORM_NAME_INVALID"
    
    FORM_TEMPLATE_NOT_FOUND = "FORM_TEMPLATE_NOT_FOUND"
    FORM_TEMPLATE_STATUS_INVALID = "FORM_TEMPLATE_STATUS_INVALID"
    
    # Field errors
    FIELD_TYPE_INVALID = "FIELD_TYPE_INVALID"
    FIELD_NAME_DUPLICATE = "FIELD_NAME_DUPLICATE"
    FIELD_NAME_RESERVED = "FIELD_NAME_RESERVED"

class ErrorMessages:
    """Human-readable error messages (translatable)"""
    
    # User messages
    USER_NOT_FOUND = _("User does not exist")
    USER_INVALID = _("Invalid user provided")
    
    # Form template messages  
    FORM_NAME_REQUIRED = _("Form name is required")
    FORM_NAME_TOO_SHORT = _("Form name must be at least 3 characters")
    FORM_NAME_TOO_LONG = _("Form name cannot exceed 255 characters")
    FORM_NAME_INVALID = _("Form name contains invalid characters")
    
    # Field messages
    FIELD_TYPE_INVALID = _("Invalid field type selected")
    FIELD_NAME_DUPLICATE = _("Duplicate field names are not allowed")
    FIELD_NAME_RESERVED = _("Field name cannot be a reserved word")
    
     
    FORM_TEMPLATE_NOT_FOUND = _("Form template not found")
    FORM_TEMPLATE_STATUS_INVALID = _("Invalid form template status provided")
    
    
FORM_TEMPLATE_STATUS_CHOICES = ['active', 'archived', 'deleted']
FORM_RESPONSE_STATUS_CHOICES = ['pending', 'completed', 'archived', 'deleted']
FORM_FIELD_TYPE_CHOICES = [
    'text', 'email', 'textarea', 'number', 'date',
    'checkbox', 'radio', 'dropdown', 'file'
]