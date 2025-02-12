from django.db import models

# Create your models here.
class ClientDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
class BookingDB(models.Model):
    ClientName = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    AdID = models.IntegerField(null=True, blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    UserName = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)

class OrderDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Note = models.CharField(max_length=50, null=True, blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    AdID = models.IntegerField(null=True, blank=True)
    BookingID = models.IntegerField(null=True, blank=True)
