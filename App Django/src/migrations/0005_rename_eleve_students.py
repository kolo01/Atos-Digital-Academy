# Generated by Django 5.1 on 2024-08-23 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_eleve_matricula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eleve',
            new_name='Students',
        ),
    ]