from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    article = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, default='')
    manufacturer = models.CharField(max_length=100, blank=True, default='')
    barcode = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True) 
    price = models.IntegerField()
    weight = models.IntegerField()
    def __str__(self):
        return self.title

class MyUser(User):
    real_name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

class Package(models.Model):
    products = models.ManyToManyField(Product, related_name='products', symmetrical=False)
    owner = models.ForeignKey(MyUser)
    handed = models.BooleanField(default=False)
    sended = models.BooleanField(default=False)
    price = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)