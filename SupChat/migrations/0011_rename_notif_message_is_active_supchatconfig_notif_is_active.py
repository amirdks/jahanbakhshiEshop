# Generated by Django 3.2 on 2022-10-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SupChat', '0010_auto_20221003_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supchatconfig',
            old_name='notif_message_is_active',
            new_name='notif_is_active',
        ),
    ]