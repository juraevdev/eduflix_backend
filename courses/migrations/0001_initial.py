# Generated by Django 4.2 on 2025-04-02 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('duration', models.DateTimeField(blank=True, null=True)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subject')),
            ],
        ),
    ]
