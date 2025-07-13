from django.db import models
from django.utils.translation import gettext_lazy as _

from .models import FormFieldType, FormResponseStatus
from django.utils.translation import gettext_lazy as _


class FormTemplateManager(models.Manager):
    def list(self):
        return self.filter(is_active=True, deleted_at__isnull=True).order_by('created_at')
    
    def list_by_user(self, user: int):
        return self.filter(user_id=user, is_active=True, deleted_at__isnull=True).order_by('created_at')
      
    def find_by_id_and_user(self, template_id, user: int):
        """Find a template by ID and user, only active and not deleted"""
        return self.filter(id=template_id, user_id=user, is_active=True, deleted_at__isnull=True).first()
    
    def search(self, query):
        """Search in name and description"""
        if not query or not query.strip():
            return self.list_active()
            
        return self.filter(
            models.Q(name__icontains=query.strip()) |
            models.Q(description__icontains=query.strip()),
            is_active=True,
            deleted_at__isnull=True
        ).order_by('-created_at')
        

        

class FormTemplateFieldManager(models.Manager):
    def find_by_template(self, template):
        return self.filter(template=template, is_active=True, deleted_at__isnull=True)
      
    def find_by_template_and_type(self, template, field_type: FormFieldType):
        return self.filter(template=template, field_type=field_type, is_active=True, deleted_at__isnull=True)



class FormResponseManager(models.Manager):
  
  def find_by_template(self, template):
    """Find by template, only active and not deleted responses.
    Template  is linked to a specific form and user"""
    return self.filter(template=template, is_active=True, deleted_at__isnull=True)
  
  def find_by_user(self, user):
      """Find all responses by user, only active and not deleted"""
      return self.select_related('template').filter(template__user_id=user, is_active=True, status__not_in=[FormResponseStatus.DELETED, FormResponseStatus.ARCHIVED ])

  def get_responses_by_responder_email(self, email):
      return self.filter(responder_email=email, is_active=True, deleted_at__isnull=True)
    
  def archive_response(self, response):
      """Archive a response by setting the status to ARCHIVED and updating the archived_at timestamp"""
      response.status = FormResponseStatus.ARCHIVED
      response.archived_at = models.DateTimeField(auto_now=True)
      response.save(update_fields=['status', 'archived_at'])
      return response
    
  def delete_response(self, response):
      """Soft delete a response by setting the status to DELETED and updating the deleted_at timestamp"""
      response.status = FormResponseStatus.DELETED
      response.deleted_at = models.DateTimeField(auto_now=True)
      response.save(update_fields=['status', 'deleted_at'])
      return response
    
  

class FormResponseFieldManager(models.Manager):
    def find_by_response(self, response):
        """Find all fields for a specific response"""
        return self.filter(form_response=response, is_active=True, deleted_at__isnull=True)
    
    def find_by_field_name(self, response, field_name):
        """Find a specific field by name in a response"""
        return self.filter(form_response=response, field_name=field_name, is_active=True, deleted_at__isnull=True)
     