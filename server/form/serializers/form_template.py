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
      
    # Override create to set user_id automatically
    def save(self, validated_data):
        user = self.context['request'].user
        validated_data['user_id'] = user
        return super().create(validated_data)
      
      
class UpdateFormTemplateSerializer(ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = ['name', 'description', 'status', 'can_respond', 'can_use_multiple_times']
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')
        

    def validate_name(self, value):
      return validate_form_name(value)

      
    def validate_status(self, value):
        return validate_form_template_status(value, ['active', 'inactive'])
      
    
    def validate(self, attrs):
      # Verify user details
      user = self.context['request'].user
      template_id = self.instance.id if self.instance else None
      if template_id is None:
          raise ValidationError({
              'code': ErrorCodes.FORM_TEMPLATE_NOT_FOUND,
              'message': ErrorMessages.FORM_TEMPLATE_NOT_FOUND,
              'field': 'id'
          })
      template: FormTemplate | None = FormTemplate.objects.find_by_id_and_user(template_id, user.id)
      if not template:
          raise ValidationError({
              'code': ErrorCodes.FORM_TEMPLATE_NOT_FOUND,
              'message': ErrorMessages.FORM_TEMPLATE_NOT_FOUND,
              'field': 'id'
          })
      return attrs


      
    # Override create to set user_id automatically
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user_id'] = user
        return super().create(validated_data)
      
      
class DeleteFormTemplateSerializer(ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = []

        
    def validate(self, attrs):
        user = self.context['request'].user
        template_id = attrs.get('id')
        if not template_id:
            raise ValidationError({
                'code': ErrorCodes.FORM_TEMPLATE_NOT_FOUND,
                'message': ErrorMessages.FORM_TEMPLATE_NOT_FOUND,
                'field': 'id'
            })
        template: FormTemplate | None = FormTemplate.objects.find_by_id_and_user(template_id, user.id)
        if not template:
            raise ValidationError({
                'code': ErrorCodes.FORM_TEMPLATE_NOT_FOUND,
                'message': ErrorMessages.FORM_TEMPLATE_NOT_FOUND,
                'field': 'id'
            })
        return attrs
