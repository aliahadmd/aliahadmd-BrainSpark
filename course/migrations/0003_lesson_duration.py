# Generated by Django 5.0.6 on 2024-07-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='duration',
            field=models.PositiveIntegerField(blank=True, help_text='Duration in minutes', null=True),
        ),
    ]
