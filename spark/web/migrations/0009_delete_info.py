# Generated by Django 5.1.1 on 2024-12-11 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_rename_id_info_sn'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
    ]