from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100,  unique=True, verbose_name="name")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Manufacturer")
    country = models.ForeignKey(Country, related_name='manufacturers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Car")
    manufacturer = models.ForeignKey(Manufacturer, related_name='cars', on_delete=models.CASCADE)
    date_created = models.DateField()
    date_finished = models.DateField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    email = models.EmailField(verbose_name="Email")
    car = models.ForeignKey(Car, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(default=None, verbose_name="Comment")

    def __str__(self):
        return self.comment

    