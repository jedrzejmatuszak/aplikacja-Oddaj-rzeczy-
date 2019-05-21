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


class Clothes(models.Model):
    type = models.CharField(max_length=128, choices=CLOTHES)
    for_who = models.CharField(max_length=128, choices=FOR_WHO)
    purpose = models.CharField(max_length=128, choices=PURPOSE)
    toys = models.CharField(max_length=128, choices=GENDER)
    books = models.CharField(max_length=128, choices=BOOKS)
    others = models.TextField()
