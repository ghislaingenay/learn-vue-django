from rest_framework.serializers import ValidationError,ModelSerializer

from form.models import FormTemplate, FormTemplateStatus
from form.constants import ErrorCodes, ErrorMessages
from form.validators import validate_form_name, validate_form_template_status
from users.models import User
from django.utils.translation import gettext_lazy as _


  

class CreateFormTemplateSerializer(ModelSerializer):
    class Meta:
        model = FormTemplate
        exclude = ['created_at', 'updated_at', 'deleted_at', 'user_id', 'fields']
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')
        

      
    def validate_name(self, value):
        return validate_form_name(value)
      
    def validate_status(self, value):
        return validate_form_template_status(value, ['active', 'inactive'])
      

      
class UpdateFormTemplateSerializer(ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = ['name', 'description', 'status', 'can_respond', 'can_use_multiple_times']
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')
        

    def validate_name(self, value):
      return validate_form_name(value)

      
    def validate_status(self, value):
        return validate_form_template_status(value, ['active', 'inactive'])
      
    



class DeleteFormTemplateSerializer(ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = []

   
class FormTemplateListSerializer(ModelSerializer):

    class Meta:
        model = FormTemplate
        fields = ['status']
        
    def validate_status(self, value):
      return validate_form_template_status(value, ['active', 'inactive'])
      

