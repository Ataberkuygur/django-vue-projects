# Generated by Django 3.2.2 on 2021-05-08 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Day', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='category',
        ),
    ]
