# Generated by Django 3.2.12 on 2022-05-15 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vac_drive', '0008_remove_studentvaccination_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentvaccination',
            name='student',
            field=models.ForeignKey(default=1111, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Student', to='vac_drive.student'),
            preserve_default=False,
        ),
    ]
