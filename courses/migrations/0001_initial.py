# Generated by Django 4.2 on 2025-04-06 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course/images/')),
                ('duration', models.DateTimeField(blank=True, null=True)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course_type', models.CharField(blank=True, choices=[('Ingliz tili', 'ingliz tili'), ('Rus tili', 'rus tili'), ('Ona tili', 'Ona tili'), ('Matematika', 'matematike'), ('Adabiyot', 'adabiyot')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('teacher', models.ManyToManyField(blank=True, limit_choices_to={'role': 'teacher'}, related_name='course_teachers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='groups/images/')),
                ('start_time', models.DateField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.course')),
                ('pupils', models.ManyToManyField(blank=True, limit_choices_to={'role': 'pupil'}, related_name='pupils', related_query_name='pupils', to=settings.AUTH_USER_MODEL)),
                ('teachers', models.ManyToManyField(blank=True, limit_choices_to={'role': 'teacher'}, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
