from django.db import models



class Subject(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)


class Course(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    duration = models.DateTimeField(null=True, blank=True)
    fee = models.DecimalField(decimal_places=2, max_digits=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.fee}'
    
