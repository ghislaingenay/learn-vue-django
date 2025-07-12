from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(_("Password"),max_length=128)
    first_name = models.CharField(_("First name"),max_length=30, blank=True)
    last_name = models.CharField(_("Last name"),max_length=30, blank=True)
    role = models.CharField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Remove 'email' and 'password' from here
    
    objects = CustomUserManager()  # Don't forget your custom manager
    
    
    # def save(self, **kwargs):
    #     do_something()
    #     super().save(**kwargs)  # Call the "real" save() method.
    #     do_something_else()
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        indexes = [models.Index(fields=['email'])]
        ordering = ['email']


## Should provide a validtation method to ensure that the user cannot have a blank password.
    # def clean(self):
    #     if not self.password:
    #         raise ValidationError("Password cannot be blank.")
        # Additional validation logic can be added here if needed.
#  def clean(self):
#         # Don't allow draft entries to have a pub_date.
#         if self.status == "draft" and self.pub_date is not None:
#             raise ValidationError(_("Draft entries may not have a publication date."))
#         # Set the pub_date for published items if it hasn't been set already.
#         if self.status == "published" and self.pub_date is None:
#             self.pub_date = datetime.date.today()