# Generated by Django 3.2.12 on 2022-05-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac_drive', '0003_auto_20220515_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvaccination',
            name='vaccinationDate',
            field=models.DateField(),
        ),
    ]
