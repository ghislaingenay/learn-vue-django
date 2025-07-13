from django.shortcuts import get_object_or_404
from server.form.enums import FormTemplateStatus
from server.form.models import FormResponse, FormTemplate
from rest_framework import viewsets
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied, ValidationError
from server.form.serializers.form_template import CreateFormTemplateSerializer, DeleteFormTemplateSerializer, FormTemplateListSerializer, UpdateFormTemplateSerializer
from server.formsystem.utils.http_response_body import success_response


class FormTemplateViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Form Templates.
    Provides CRUD operations and ensures user ownership.
    """
    
    def get_queryset(self):
      """Only return templates owned by current user"""
      return FormTemplate.objects.filter(
          user_id=self.request.user,
          status__in=[FormTemplateStatus.ACTIVE, FormTemplateStatus.INACTIVE]
      ).order_by('-created_at')
      
    def get_object(self):
        # Override to ensure user owns the template
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj
      
    def get_serializer_class(self):
      """Return appropriate serializer based on action"""
      if self.action == 'create':
        return CreateFormTemplateSerializer
      elif self.action in ['update', 'partial_update']:
        return UpdateFormTemplateSerializer
      elif self.action == 'destroy':
        return DeleteFormTemplateSerializer  # Use same serializer for deletion
      else:
        return FormTemplateListSerializer  # For list, retrieve
      
    def perform_create(self, serializer):
      """
      ✅ Set user automatically during creation
      Called by create() method
      """
      serializer.save(user_id=self.request.user)
      
      
    @action(detail=, methods=['post'])
    def archive(self, request, *args, **kwargs):
        """Custom action to archive a form template"""
        template_id = self.kwargs.get('pk')
        template = self._have_template_access(template_id)
        template.status = FormTemplateStatus.ARCHIVED
        template.archived_at = timezone.now()
        template.save(update_fields=['status', 'archived_at'])
        return success_response('Template archived', None, 201)
      
    # ✅ PRIVATE METHODS - Internal logic
    
      
    def _have_template_access(self, template_id):
      """Validate user can access this template"""
      template = FormTemplate.objects.filter(id=template_id, user_id=self.request.user).first()
      if template.user_id != self.request.user:
        raise PermissionDenied("You don't have permission to access this template")
        
      if template.status == FormTemplateStatus.DELETED or template.deleted_at is not None:
        raise ValidationError("Cannot access deleted template")
      return True
    
     # Override destroy to handle soft delete
    def destroy(self, request, *args, **kwargs):
        """Soft delete a form template"""
        template_id = self.kwargs.get('pk')
        template = self._have_template_access(template_id)
        
        # Soft delete logic
        template.status = FormTemplateStatus.DELETED
        template.deleted_at = timezone.now()
        template.save(update_fields=['status', 'deleted_at'])
        
        return success_response('Template deleted', None, 204)
     
    