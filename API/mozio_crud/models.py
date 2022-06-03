from django.db import models

LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('SPA', 'Spanish'),
    ('FRA', 'French'),
    ('GER', 'German'),
]


CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'Pound'),
]


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField()
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    # (name, price, geojson information)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6 , decimal_places=2, default=0.00)
    polygon = models.TextField()
