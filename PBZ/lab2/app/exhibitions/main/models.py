from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    birth_place = models.CharField()
    birth_date = models.DateField(null=True)
    info = models.CharField()
    education = models.CharField()

    def __str__(self):
        return self.name


class Owner(models.Model):
    class OwnerType(models.TextChoices):
        CITY = 'CI', _('City organization')
        REGIONAL = 'RE', _('Regional organization')
        PUBLIC = 'PU', _('Public organization')
        PRIVATE = 'PR', _('Private organization')

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    adress = models.CharField()
    phone = models.CharField()
    type = models.CharField(max_length=2, choices=OwnerType.choices, default=OwnerType.PUBLIC)

    def __str__(self):
        return self.name

class ExhibitionHall(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    adress = models.CharField()
    phone = models.CharField()
    space = models.CharField()
    date = models.DateField(null=True)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    class ExhibitionType(models.TextChoices):
        ART = 'AR', _('Art')
        APPLIED = 'AP', _('Applied')
        SCULPTURE = 'SC', _('Sculpture')

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    type = models.CharField(max_length=2, choices=ExhibitionType.choices,default=ExhibitionType.ART)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    exhibition_hall = models.ForeignKey(ExhibitionHall, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exhibit(models.Model):
    class ExhibitType(models.TextChoices):
        PAINTING = 'PA', _('Painting') 
        SCULPTURE = 'SC', _('Sculpture')
        ARCHITRCTURE = 'AR', _('Architecture')

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    date = models.DateField(null=True)
    size = models.CharField()
    type = models.CharField(max_length=2, choices=ExhibitType.choices,default=ExhibitType.PAINTING)

    exhibitions = models.ManyToManyField(Exhibition)
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    

    