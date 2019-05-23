from django.db import models

# Create your models here.
CLOTHES = (
    ('1', 'ubrania, które nadają się do ponownego użycia'),
    ('2', 'ubrania do wyrzucenia'),
    ('3', 'zabawki'),
    ('4', 'książki'),
    ('5', 'inne')
)

FOR_WHO = (
    ('1', 'Męskie'),
    ('2', 'Damskie'),
    ('3', 'Dziecięce dla dziewczynki'),
    ('4', 'Dziecięce dla chłopca')
)

PURPOSE = (
    ('1', 'Sezon jesień-zima'),
    ('2', 'Sezon wiosna-lato')
)

GENDER = (
    ('1', 'Chłopiec'),
    ('2', 'Dziewczynka')
)

AGE = (
    ('1', '0-2'),
    ('2', '3-5'),
    ('3', '6-8'),
    ('4', '9-12'),
    ('5', '12-15'),
    ('6', '15+')
)

BOOKS = (
    ('1', 'dla dorosłych'),
    ('2', 'dla dzieci'),
    ('3', 'dla młodzieży'),
    ('4', 'edukacyjne')
)

NUMBER = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '>10'),
)

LOCATION = (
    ('1', 'dolnośląskie'),
    ('2', 'kujawsko-pomorskie'),
    ('3', 'lubelskie'),
    ('4', 'lubuskie'),
    ('5', 'łódzkie'),
    ('6', 'małopolskie'),
    ('7', 'mazowieckie'),
    ('8', 'opolskie'),
    ('9', 'podkarpackie'),
    ('10', 'podlaskie'),
    ('11', 'pomorskie'),
    ('12', 'śląskie'),
    ('13', 'świętokrzyskie'),
    ('14', 'warmińsko-mazurskie'),
    ('15', 'wielkopolskie'),
    ('16', 'zachodniopomorskie'),
)

HELP = (
    ('1', 'dzieciom'),
    ('2', 'samotnym matkom'),
    ('3', 'bezdomnym'),
    ('4', 'niepełnosprawnym'),
    ('5', 'osobom starszym'),
    ('6', 'bezrobotnym'),
)


class Clothes(models.Model):
    type = models.CharField(max_length=128, choices=CLOTHES)
    for_who = models.CharField(max_length=128, choices=FOR_WHO)
    purpose = models.CharField(max_length=128, choices=PURPOSE)
    toys = models.CharField(max_length=128, choices=GENDER)
    books = models.CharField(max_length=128, choices=BOOKS)
    others = models.TextField()


class Bags(models.Model):
    number_of_bugs = models.CharField(max_length=4, choices=NUMBER)


class Charity(models.Model):
    location = models.CharField(max_length=50, choices=LOCATION)
    help = models.CharField(max_length=100, choices=HELP)
    charity_name = models.CharField(max_length=255)


class Address(models.Model):
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=6)
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField()
