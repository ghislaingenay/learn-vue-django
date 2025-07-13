from django.shortcuts import render
from rest_framework.views import APIView

from formsystem.utils.http_response_body import error_response
from users.models import User

from rest_framework_simplejwt.views import TokenObtainPairView


class JSONAPITokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Extract email/password from JSON:API format
        if 'data' in request.data and 'attributes' in request.data['data']:
            request.data = request.data['data']['attributes']
        return super().post(request, *args, **kwargs)
    
