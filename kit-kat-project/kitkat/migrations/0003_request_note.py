# Generated by Django 2.2.3 on 2019-07-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0002_auto_20190722_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='note',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]