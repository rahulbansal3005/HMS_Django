# Generated by Django 3.0.6 on 2020-09-21 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20200920_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outing',
            options={'ordering': ['-fromDate']},
        ),
    ]