from rest_framework.serializers import ValidationError,ModelSerializer

from form.models import FormTemplate, FormTemplateStatus
from form.constants import ErrorCodes, ErrorMessages
from users.models import User
from django.utils.translation import gettext_lazy as _

class CreateFormTemplateSerializer(ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')
        
    def validate_user_id(self, value):
        user = User.objects.filter(id=value.id).first()
        if not user:
              raise ValidationError({
                'code': ErrorCodes.USER_NOT_FOUND,
                'message': ErrorMessages.USER_NOT_FOUND,
                'field': 'user_id'
            })
        return value
      
    def validate_name(self, value):
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
      
    def validate_status(self, value):
        if value not in [status[0] for status in FormTemplateStatus.choices]:
            raise ValidationError({
                "code": ErrorCodes.FORM_TEMPLATE_STATUS_INVALID,
                "message": ErrorMessages.FORM_TEMPLATE_STATUS_INVALID,
                "field": "status"
            })
        return value
      
    def validate(self, attrs):
        if attrs.get('deleted_at') is not None and attrs.get('status') != FormTemplateStatus.DELETED:
            raise ValidationError({
                "code": ErrorCodes.FORM_TEMPLATE_STATUS_INVALID,
                "message": ErrorMessages.FORM_TEMPLATE_STATUS_INVALID,
                "field": "status"
            })
      
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user_id'] = user
        return super().create(validated_data)