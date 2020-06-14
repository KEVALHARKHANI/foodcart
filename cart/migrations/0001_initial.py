# Generated by Django 3.0.6 on 2020-05-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expiry_date', models.CharField(max_length=200)),
                ('card_number', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
