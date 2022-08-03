# Generated by Django 4.1 on 2022-08-03 14:04

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number_or_email', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('pronoun', models.CharField(blank=True, max_length=20, null=True)),
                ('option_gender', models.CharField(blank=True, max_length=25, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
