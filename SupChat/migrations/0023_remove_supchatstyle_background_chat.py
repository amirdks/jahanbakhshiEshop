# Generated by Django 3.2 on 2022-10-12 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SupChat', '0022_alter_supchatstyle_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supchatstyle',
            name='background_chat',
        ),
    ]
