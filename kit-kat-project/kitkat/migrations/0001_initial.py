# Generated by Django 2.2.3 on 2019-07-22 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('team', models.CharField(choices=[('ENG', 'Engineering'), ('PROD', 'Product'), ('PS', 'Partner Success'), ('SALE', 'Sales')], max_length=50)),
                ('user_type', models.CharField(choices=[('EMP', 'Employee'), ('MAN', 'Manager')], default='EMP', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ENG', 'Engineering'), ('PROD', 'Product'), ('PS', 'Partner Success'), ('SALE', 'Sales')], max_length=25)),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager_of', to='kitkat.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('hours', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitkat.Profile')),
            ],
        ),
    ]
