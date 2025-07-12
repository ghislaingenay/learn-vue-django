# middleware.py (create in your project root or users app)
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
import re

class ConditionalJWTMiddleware(MiddlewareMixin):
    """
    Middleware that checks JWT tokens only on specific routes
    """
    
    # Define routes that require JWT authentication
    PROTECTED_ROUTES = [
        r'^/api/users/me/$',
        r'^/api/forms/',
        r'^/api/protected/',
        # Add more patterns as needed
    ]
    
    def process_request(self, request):
        # Check if current path matches any protected route
        current_path = request.path
        is_protected = any(re.match(pattern, current_path) for pattern in self.PROTECTED_ROUTES)
        
        if not is_protected:
            return None  # Skip JWT validation for non-protected routes
        
        # Check for JWT token
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse(
                {'error': 'Authentication required'}, 
                status=401
            )
        
        try:
            # Validate JWT token
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(auth_header.split(' ')[1])
            user = jwt_auth.get_user(validated_token)
            request.user = user
            request.auth = validated_token
        except (InvalidToken, TokenError) as e:
            return JsonResponse(
                {'error': 'Invalid or expired token'}, 
                status=401
            )
        
        return None