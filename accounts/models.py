from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager

ROLE_CHOICES = [
    ("admin", "Administrator"),
    ("manager", "Manager"),
    ("accountant", "Accountant")
]

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default="manager")

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['name', 'role']
    USERNAME_FIELD  = 'email'

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"