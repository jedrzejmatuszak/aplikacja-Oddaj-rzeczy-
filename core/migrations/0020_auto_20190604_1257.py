# Generated by Django 2.2.1 on 2019-06-04 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190604_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bags',
            old_name='number_of_bugs',
            new_name='number_of_bags',
        ),
    ]
