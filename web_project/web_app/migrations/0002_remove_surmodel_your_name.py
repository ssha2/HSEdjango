# Generated by Django 5.0.2 on 2024-05-26 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surmodel',
            name='your_name',
        ),
    ]