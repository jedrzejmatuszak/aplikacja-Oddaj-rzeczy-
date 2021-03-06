# Generated by Django 2.2.1 on 2019-05-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'ubrania, które nadają się do ponownego użycia'), ('2', 'ubrania do wyrzucenia'), ('3', 'zabawki'), ('4', 'książki'), ('5', 'inne')], max_length=128)),
                ('for_who', models.CharField(choices=[('1', 'Męskie'), ('2', 'Damskie'), ('3', 'Dziecięce dla dziewczynki'), ('4', 'Dziecięce dla chłopca')], max_length=128)),
                ('purpose', models.CharField(choices=[('1', 'Sezon jesień-zima'), ('2', 'Sezon wiosna-lato')], max_length=128)),
                ('toys', models.CharField(choices=[('1', 'Chłopiec'), ('2', 'Dziewczynka')], max_length=128)),
                ('books', models.CharField(choices=[('1', 'dla dorosłych'), ('2', 'dla dzieci'), ('3', 'dla młodzieży'), ('4', 'edukacyjne')], max_length=128)),
                ('others', models.TextField()),
            ],
        ),
    ]
