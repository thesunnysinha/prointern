# Generated by Django 4.0.2 on 2022-02-13 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0002_remove_users_middle_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
