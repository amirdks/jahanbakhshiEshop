# Generated by Django 3.2 on 2022-10-05 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SupChat', '0012_auto_20221003_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='data_time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]