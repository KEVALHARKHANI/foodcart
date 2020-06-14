# Generated by Django 2.2.6 on 2020-05-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagery', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('specialoffer', models.BooleanField()),
                ('offer', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=500)),
                ('opentime', models.TimeField()),
            ],
        ),
    ]