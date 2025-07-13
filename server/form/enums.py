from django.db import models
from django.utils.translation import gettext_lazy as _

class FormFieldType(models.TextChoices):
    TEXT = 'text', _('Text')
    EMAIL = 'email', _('Email')
    TEXTAREA = 'textarea', _('Text Area')
    NUMBER = 'number', _('Number')
    DATE = 'date', _('Date')
    CHECKBOX = 'checkbox', _('Checkbox')
    RADIO = 'radio', _('Radio Button')
    DROPDOWN = 'dropdown', _('Dropdown')
    FILE = 'file', _('File Upload')


class FormResponseStatus(models.TextChoices):
    PENDING = 'pending', _('Pending')
    COMPLETED = 'completed', _('Completed')
    ARCHIVED = 'archived', _('Archived')
    DELETED = 'deleted', _('Deleted')
    
class FormTemplateStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    INACTIVE = 'inactive', _('Inactive')
    DELETED = 'deleted', _('Deleted')
    