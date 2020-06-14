# Generated by Django 3.0.6 on 2020-06-12 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_auto_20200612_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]