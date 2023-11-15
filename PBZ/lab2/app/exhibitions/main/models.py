from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Artists(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    birth_place = models.CharField()
    birth_date = models.DateField(null=True)
    info = models.CharField()
    education = models.CharField()


class Owners(models.Model):
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


class ExhibitionHalls(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    adress = models.CharField()
    phone = models.CharField()
    space = models.CharField()
    date = models.DateField(null=True)
    owner_id = models.ForeignKey(Owners, null=True, on_delete=models.SET_NULL)


class Exhibitions(models.Model):
    class ExhibitionType(models.TextChoices):
        ART = 'AR', _('Art')
        APPLIED = 'AP', _('Applied')
        SCULPTURE = 'SC', _('Sculpture')

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    type = models.CharField(max_length=2, choices=ExhibitionType.choices,default=ExhibitionType.ART)
    date = models.DateField(null=True)
    exhibition_hall_id = models.ForeignKey(ExhibitionHalls, on_delete=models.CASCADE)


class Exhibits(models.Model):
    class ExhibitType(models.TextChoices):
        PAINTING = 'PA', _('Painting') 
        SCULPTURE = 'SC', _('Sculpture')
        ARCHITRCTURE = 'AR', _('Architecture')

    id = models.AutoField(primary_key=True)
    name = models.CharField()
    date = models.DateField(null=True)
    size = models.CharField()
    type = models.CharField(max_length=2, choices=ExhibitType.choices,default=ExhibitType.PAINTING)

    exhibitions = models.ManyToManyField(Exhibitions)
    artist_id = models.ForeignKey(Artists, null=True, on_delete=models.SET_NULL)
    

    