# Generated by Django 3.2 on 2022-10-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupChat', '0009_auto_20220930_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supchatconfig',
            old_name='notif_message',
            new_name='default_notif_message',
        ),
        migrations.RenameField(
            model_name='supchatconfig',
            old_name='notif_message_show_after',
            new_name='default_notif_message_show_after',
        ),
        migrations.AddField(
            model_name='supchatconfig',
            name='default_notif_message_is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='supchatconfig',
            name='notif_sound_is_active',
            field=models.BooleanField(default=True),
        ),
    ]
