# Generated by Django 2.2.3 on 2019-07-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0003_auto_20190721_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='hours',
            field=models.IntegerField(blank=True),
        ),
    ]