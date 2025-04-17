import random, datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager 


ROLE_CHOICES = [
    ("admin", "Administrator"),
    ("manager", "Manager"),
    ("accountant", "Accountant"),
    ("teacher", "Teacher"),
    ("pupil", "Pupil"),
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
    

    def generate_verify_code(self):
        code = ''.join(str(random.randint(0, 9)) for _ in range(5))
        ConfirmationCodes.objects.create(
            user = self,
            code=code,
            expires = timezone.now() + datetime.timedelta(minutes=2)
        )
        return code
    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='pupil')
    coin = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=14, null=True)


    def __str__(self):
        return f'{self.first_name} - {self.last_name}'    
    
    
class ConfirmationCodes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='codes')
    code = models.CharField(max_length=5)
    expires = models.DateTimeField(null=True, blank=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.code}"


class AdminProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin')
    image = models.ImageField(upload_to='admin/profile_images/')
    subject = models.CharField(max_length=50, null=True, blank=True)
    subject_cost = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    cost_share = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    students = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    monthly_payment = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    benefit = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)


class CoinHistory(models.Model):
    COIN_ACTIONS = [
        ("attend", "Darsga vaqtida kelish"),
        ("homework", "Uyga vazifa bajarish"),
        ("extra_task", "Qo'shimcha vazifa bajarish"),
        ("bring_friend", "Do'stini olib kelish"),
        ("perfect_month", "Mukammal qatnashuv"), 
        ("no_task", "Vazifa bajarmaslik"),
        ("miss_class", "Darsni o'tkazib yuborish"),
    ]

    ACTION_COIN_MAP = {
        "attend": 1,
        "homework": 2,
        "extra_task": 3,
        "bring_friend": 5,
        "perfect_month": 10,
        "no_task": -3,
        "miss_class": -2,
    }

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='coin_history')
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'teacher'})
    action = models.CharField(max_length=20, choices=COIN_ACTIONS)
    coin = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.coin:
            self.coin = self.ACTION_COIN_MAP.get(self.action, 0)
        super().save(*args, **kwargs)

        self.student.coin = (self.student.coin or 0) + self.coin    
        self.student.save()


    def __str__(self):
        return f"{self.student} - {self.action} ({self.coin} coin)"
    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'teacher'})
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=True)

    class Meta:
        unique_together = ['student', 'date']
        verbose_name = "Davomat"
        verbose_name_plural = "Davomatlar"

    
    def __str__(self):
        return f'{self.student} - {"Keldi" if self.is_present else "Kelmadi"} - {self.date}'
        