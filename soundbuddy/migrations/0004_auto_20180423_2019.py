# Generated by Django 2.0.3 on 2018-04-23 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soundbuddy', '0003_auto_20180422_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='adress',
            new_name='address',
        ),
    ]
