# Generated by Django 4.1.1 on 2022-09-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='SelectWorkout',
            new_name='SelectAsanas',
        ),
    ]
