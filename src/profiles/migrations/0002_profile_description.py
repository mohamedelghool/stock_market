# Generated by Django 2.0.1 on 2018-01-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='description default text'),
        ),
    ]
