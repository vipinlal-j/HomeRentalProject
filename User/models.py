from django.db import models

# Create your models here.
class userDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(max_length=10, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)

class user1DB(models.Model):
    email = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

class PostDB(models.Model):
    Category = models.CharField(max_length=50, null=True, blank=True)
    Rooms = models.IntegerField(max_length=2, null=True, blank=True)
    Kitchen = models.CharField(max_length=3, null=True, blank=True)
    Information = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Rent = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(max_length=10, null=True, blank=True)
    Image = models.ImageField(upload_to='media/',null=True, blank=True)

class ImageDB(models.Model):
    Img = models.ImageField(null=True, blank=True)