# Generated by Django 3.2.9 on 2021-11-23 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='creatad_on',
            new_name='created_on',
        ),
    ]
