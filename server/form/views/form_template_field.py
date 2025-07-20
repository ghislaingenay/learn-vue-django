from requests import Response
from rest_framework.views import APIView
from server.form.models import FormTemplateField
from server.form.serializers.form_template_field import CreateFormTemplateFieldSerializer, UpdateFormTemplateFieldSerializer
from datetime import timezone
class FormTemplateFieldViewPerTemplate(APIView):
  
  def get(self, request, *args, **kwargs):
    """ Get fields for one spefic template"""
    # Logic to handle GET request for form template fields
    user_id = request.user.id
    template_id = kwargs.get('template_id')
    if not template_id:
      return Response({"details": "Template ID is required"}, status=400)
    valid_template = FormTemplateField.objects.filter(
        template__id=template_id,
        template__user_id=user_id,
        template__deleted_at__isnull=True
    ).exists()
    
    if not valid_template:
      return Response({"details": "Invalid template ID or you do not have access to this template"}, status=404)
    template_fields = FormTemplateField.objects.filter(
        template__id=template_id,
        template__user_id=user_id,
        template__deleted_at__isnull=True
    ).values('id', 'field_name', 'field_type', 'required', 'is_editable', 'is_active', 'options', 'restrictions', 'default_value')

    return Response({"details": "GET request for form template fields", "data": template_fields}, status=200)
  
  
class FormTemplateFieldView(APIView):
  
  def post(self, request, *args, **kwargs):
    """Create a new form template field"""
    template_id = kwargs.get('template_id')
    if not template_id:
      return Response({"details": "Template ID is required"}, status=400)
    user_id = request.user.id
    valid_template = FormTemplateField.objects.filter(
        template__id=template_id,
        template__user_id=user_id,
        template__deleted_at__isnull=True
    ).exists()
    if not valid_template:
      return Response({"details": "Invalid template ID or you do not have access to this template"}, status=404)
    serializer = CreateFormTemplateFieldSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      field = serializer.save()
      return Response({"details": "Field created successfully", "data": field}, status=201)
    return Response({"details": "Invalid data", "errors": serializer.errors}, status=400)
  
  def put(self, request, *args, **kwargs):
    """Update an existing form template field"""
    field_id = kwargs.get('field_id')
    if not field_id:
      return Response({"details": "Field ID is required"}, status=400)
    user_id = request.user.id
    field = FormTemplateField.objects.filter(id=field_id, template__user_id=user_id).first()
    
    if not field:
      return Response({"details": "Field not found or you do not have permission to update it"}, status=404)
    
    serializer = UpdateFormTemplateFieldSerializer(field, data=request.data, context={'request': request})
    if serializer.is_valid():
      updated_field = serializer.save()
      return Response({"details": "Field updated successfully", "data": updated_field}, status=200)
    
    return Response({"details": "Invalid data", "errors": serializer.errors}, status=400)
  
  
  def delete(self, request, *args, **kwargs):
    """Delete a form template field"""
    field_id = kwargs.get('field_id')
    if not field_id:
      return Response({"details": "Field ID is required"}, status=400)
    
    user_id = request.user.id
    field = FormTemplateField.objects.filter(id=field_id, template__user_id=user_id).first()
    
    if not field:
      return Response({"details": "Field not found or you do not have permission to delete it"}, status=404)
    
    field.deleted_at = timezone.now()  # Soft delete
    field.save()
    
    return Response({"details": "Field deleted successfully"}, status=204)
    