from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)
