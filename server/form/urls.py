from .views import FormTemplateViewSet
from django.urls import re_path

urlpatterns = [
  # fields ID will be performed using API ViewSet
  re_path(r'^forms/templates',FormTemplateViewSet, basename='form-template'),
]