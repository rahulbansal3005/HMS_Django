# Generated by Django 3.0.6 on 2020-11-06 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institute', '0004_auto_20201104_1250'),
        ('complaints', '0002_complaint_complainee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='entity_id',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='entity_type',
        ),
        migrations.RemoveField(
            model_name='medicalissue',
            name='entity_id',
        ),
        migrations.RemoveField(
            model_name='medicalissue',
            name='entity_type',
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalissue',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institute.Student'),
        ),
    ]
