# Generated by Django 2.0.1 on 2018-01-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0005_auto_20180129_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='my location', max_length=120, null=True),
        ),
    ]
