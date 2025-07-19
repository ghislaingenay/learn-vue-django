from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from .manager import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = None  # Disable username field
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # You are seeing these errors because your custom User model inherits from PermissionsMixin, which adds groups and user_permissions fields. Django’s default auth.User model also defines these fields, causing reverse accessor clashes.
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changed from default 'user_set'
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Changed from default 'user_set'
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    
    objects = UserManager()
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