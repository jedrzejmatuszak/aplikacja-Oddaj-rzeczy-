# Generated by Django 2.2.1 on 2019-05-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190527_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='charity_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
