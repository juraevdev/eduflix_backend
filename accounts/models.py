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


class AdminProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin')
    image = models.ImageField(upload_to='admin/profile_images/')
    subject = models.CharField(max_length=50, null=True, blank=True)
    subject_cost = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    cost_share = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    students = models.CharField(max_length=50, null=True, blank=True)
    monthly_payment = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    benefit = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    
