# Generated by Django 5.1 on 2024-08-22 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='matricule',
        ),
    ]
