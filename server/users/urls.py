from django.urls import path, include
from .views import RegisterView

urlpatterns = [
  # path('me', CurrentUserView.as_view(),name='me'),
  # path('login', LoginView.as_view(), name='login'),
  # path('logout',LogoutView.as_view(), name='logout'),
  path('register', RegisterView.as_view(), name='register'),
    # path('api/auth/', include('users.urls'), name='auth'),
]