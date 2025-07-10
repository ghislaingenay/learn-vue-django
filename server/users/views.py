from django.shortcuts import render
from rest_framework.views import APIView

from formsystem.utils.http_response_body import error_response
from users.models import User

# Create your views here.
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.data.get('email'))
        if user:
            return error_response("User already exists", status_code=400)
        # Logic for user registration
        return Response({"message": "User registered successfully"}, status=201)
    
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.data.get('email'))
        if not user:
            return Response({"message": "User does not exist", "isSuccess": False}, status=404)
        # Logic for user login
        return Response({"message": "User logged in successfully"}, status=200)