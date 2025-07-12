from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
  
  def email_validator(self, email):
    try:
      validate_email(email)
    except ValidationError:
      raise ValidationError(_("Invalid email address"))
    
  def create_user(self, first_name, last_name, email, password=None, **extra_fields):
    if not first_name or not last_name:
      raise ValueError(_("First name and/or last name are required"))
    if not email:
      raise ValueError(_("Email is required"))
    email = self.normalize_email(email)
    self.email_validator(email)
    
    user = self.model(first_name=first_name, last_name=last_name, email=email,**extra_fields)
    user.set_password(password)
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    user.save()
    return user
  
  def create_superuser(self, first_name, last_name, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)  # Sets to True if not provided
    extra_fields.setdefault('is_active', True)
    
    # Safety check - ensure is_superuser is actually True
    if extra_fields.get("is_superuser") is not True:
      raise ValueError(_("Superuser must have is_superuser=True."))
    
    if not password:
      raise ValueError(_("Password is required for superuser creation"))
    
    if not email:
      raise ValueError(_("Email is required"))
    email = self.normalize_email(email)
    self.email_validator(email)
    
    user = self.create_user(first_name, last_name, email, password, **extra_fields)
    user.save()
    return user
    
    