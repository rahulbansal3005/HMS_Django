# Generated by Django 3.0.5 on 2020-05-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20200514_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='designation',
            field=models.CharField(choices=[('Scavenger', 'Scavenger'), ('General Servant', 'General Servant'), ('Doctor', 'Doctor'), ('Mess Incharge', 'Mess Incharge'), ('Electrician', 'Electrician'), ('Gym Trainer', 'Gym Trainer'), ('PT/Games Coach', 'PT/Games Coach')], max_length=50),
        ),
    ]
