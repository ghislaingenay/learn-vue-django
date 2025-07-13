from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import FormResponseFieldManager, FormResponseManager, FormTemplateManager, FormTemplateFieldManager
from server.users.models import User

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
    
# Create your models here.
class FormTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=FormTemplateStatus.choices,
        default=FormTemplateStatus.ACTIVE,
        verbose_name=_('Template Status')
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='form_templates')
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete
    can_respond = models.BooleanField(default=True)  # Whether the form can accept responses
    can_use_multiple_times = models.BooleanField(default=True)  # Whether the form can be reused
    
    objects = FormTemplateManager()

    def __str__(self):
        return self.name
      
    class Meta: 
        verbose_name = _('Form Template')
        verbose_name_plural = _('Form Templates')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='form_template_name_idx'),
            models.Index(fields=['type'], name='form_template_type_idx'),
        ]
      


class FormTemplateField(models.Model):
    template = models.ForeignKey(FormTemplate, related_name='fields', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)
    is_editable = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete
    options = models.JSONField(default=list, blank=True)  # For dropdowns or checkboxes
    restrictions = models.JSONField(default=dict)  # Store restrictions as JSON
    field_type = models.CharField(
        max_length=20,
        choices=FormFieldType.choices,
        default=FormFieldType.CHECKBOX,
        verbose_name=_('Form Type')
    )
    
    default_value =models.TextField(blank=True, null=True)  # Default value for the field

    def __str__(self):
        return f"{self.field_name} ({self.field_type})"
    
    objects = FormTemplateFieldManager()
    
    class Meta:
        verbose_name = _('Form Template Field')
        verbose_name_plural = _('Form Template Fields')
        unique_together = ('template', 'field_name')  # Ensure no duplicate field names in the same template
        indexes = [
            models.Index(fields=['template'], name='form_template_idx')
        ]


class FormResponse(models.Model):
  template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
  responder_email = models.EmailField()
  responder_full_name = models.CharField(max_length=255, blank=True, null=True)
  feedback_note = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  archived_at = models.DateTimeField(null=True, blank=True)  # Soft delete
  deleted_at = models.DateTimeField(null=True, blank=True)  # Soft deletes
  access_code = models.CharField(max_length=255, blank=True, null=True)  # For sharing responses and access the current link as well
  status = models.CharField(
      max_length=20,
      choices=FormResponseStatus.choices,
      default=FormResponseStatus.PENDING,
      verbose_name=_('Response Status')
    )
  
  @property
  def is_completed(self):
      return self.status == FormResponseStatus.COMPLETED
  
  objects = FormResponseManager()
  
  
  class Meta:
      verbose_name = _('Form Response')
      verbose_name_plural = _('Form Responses')
      indexes = [
          models.Index(fields=['template'], name='form_response_template_idx'),
          models.Index(fields=['created_at'], name='form_response_created_at_idx'),
      ]
 
class FormFieldResponse(models.Model):

      
    form_response = models.ForeignKey(FormResponse, related_name='field_responses', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)
    is_editable = models.BooleanField(default=True)
    options = models.JSONField(default=list, blank=True)  # For dropdowns or checkboxes
    restrictions = models.JSONField(default=dict)  # Store restrictions as JSON
    field_type = models.CharField(
        max_length=20,
        choices=FormFieldType.choices,
        default=FormFieldType.CHECKBOX,
        verbose_name=_('Form Type')
    )
    
    value =models.TextField(blank=True, null=True)  # Default value for the field
    
    class Meta:
        verbose_name = _('Form Field Response')
        verbose_name_plural = _('Form Field Responses')
        unique_together = ('form_response', 'field_name')
        indexes = [
            models.Index(fields=['form_response'], name='form_field_response_idx')
        ]
        
    objects = FormResponseFieldManager()
