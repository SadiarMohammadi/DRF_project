# Generated by Django 5.0.3 on 2024-03-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
