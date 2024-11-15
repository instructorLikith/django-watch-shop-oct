from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Watches(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price= models.FloatField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class WatchesUploads(models.Model):
    name = models.CharField(max_length = 100) 
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='watches_images/')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

