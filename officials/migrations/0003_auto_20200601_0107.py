# Generated by Django 3.0.5 on 2020-05-31 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officials', '0002_auto_20200601_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watercan',
            old_name='receieved',
            new_name='received',
        ),
    ]
