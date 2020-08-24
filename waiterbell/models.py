from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    created_date = models.DateTimeField('date published')

class RequestType(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField('date published')

class Notification(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    open_url = models.CharField(max_length=200)
    state = models.IntegerField(default=0)
    created_date = models.DateTimeField('date published')

class Business(models.Model):
    name = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    address =  models.CharField(max_length=200)
    state = models.IntegerField(default=0)
    created_date = models.DateTimeField('date published')

class Review(models.Model):
     class EYesNo(models.TextChoices):
        YES = 'YES', _('Yes')
        NO = 'NO', _('No')

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    recommend = models.CharField( max_length=2, choices=EYesNo.choices, default=EYesNo.YES)
    approved = models.IntegerField(default=0)
    state = models.IntegerField(default=0)
    created_date = models.DateTimeField('date published')

class Rating(models.Model):
    business = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    value = models.CharField(max_length=200)


class RateType(models.Model):
    business = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    value = models.CharField(max_length=200)