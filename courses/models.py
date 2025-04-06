from django.db import models
from accounts.models import CustomUser


Course_Type = [
    ("Ingliz tili", "ingliz tili"),
    ("Rus tili", "rus tili"),
    ("Ona tili", "Ona tili"),
    ("Matematika", "matematike"),
    ("Adabiyot", "adabiyot"),
]


class Course(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='course/images/', null=True, blank=True)
    duration = models.DateTimeField(null=True, blank=True)
    fee = models.DecimalField(decimal_places=2, max_digits=10)
    teacher = models.ManyToManyField(CustomUser, blank=True, related_name="course_teachers", limit_choices_to={'role': 'teacher'})
    course_type = models.CharField(max_length=50, choices=Course_Type, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.fee}'
    

class Group(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='groups/images/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, related_name='courses')
    pupils = models.ManyToManyField(CustomUser, blank=True, related_name='pupils', limit_choices_to={'role': 'pupil'}, related_query_name='pupils')
    start_time = models.DateField(null=True, blank=True)
    teachers = models.ManyToManyField(CustomUser, blank=True, related_name='teacher', limit_choices_to={'role': 'teacher'})
    