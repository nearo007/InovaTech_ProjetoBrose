# Generated by Django 5.1 on 2024-09-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='funcionarios',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='skills',
            field=models.ManyToManyField(blank=True, to='app.skill'),
        ),
    ]
