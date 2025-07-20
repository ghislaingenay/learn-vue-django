from server.form.models import FormTemplateField
from rest_framework import serializers


class CreateFormTemplateFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplateField
        fields = ['template', 'field_name', 'required', 'is_editable', 'is_active', 'options', 'restrictions', 'field_type', 'default_value']
        required_fields = ['template', 'field_name', 'field_type']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user_id'] = user.id
        return super().create(validated_data)
      

class UpdateFormTemplateFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplateField
        fields = ['field_name', 'required', 'is_editable', 'is_active', 'options', 'restrictions','default_value']
        required_fields = ['field_name', 'field_type']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.template.user_id != user.id:
            raise serializers.ValidationError("You do not have permission to update this field.")
        return super().update(instance, validated_data)