# Generated by Django 4.0.2 on 2022-02-13 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='middle_name',
        ),
    ]
