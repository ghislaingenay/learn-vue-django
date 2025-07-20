from server.form.views.form_template_field import FormTemplateFieldViewPerTemplate
from .views import FormTemplateViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Create router for this app
router = DefaultRouter()

# Register ViewSet with router
router.register(r'templates', FormTemplateViewSet, basename='form-template')
router.register(r'templates/(?P<template_id>[^/.]+)/fields', FormTemplateFieldViewPerTemplate.as_view(), basename='form-template-field')
router.register(r'templates/(?P<template_id>[^/.]+)/fields/create', FormTemplateFieldViewPerTemplate.as_view(), basename='form-template-field')


urlpatterns = [
    # Include router URLs
    path('forms/', include(router.urls)),
]

# This creates URLs like:
# GET/POST    /forms/templates/
# GET/PUT/DELETE  /forms/templates/{id}/
# POST        /forms/templates/{id}/archive/
# POST        /forms/templates/{id}/duplicate/