# Generated by Django 4.0.5 on 2022-06-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozio_crud', '0002_servicearea_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='provider',
            new_name='provider_id',
        ),
    ]