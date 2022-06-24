import uuid
from django.db import models


class Products(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True,  blank=True)
    info = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='products', default='products\empty_cart.png', null=True)
    price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    organization = models.ForeignKey(
        'Organization', on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    material = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Images(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    image = models.ImageField(upload_to='products', default='products\empty_cart.png', null=True)
    product = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True, blank=True, related_name="images")


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='category', default='products\empty_cart.png', null=True)

    def __str__(self):
        return str(self.name)


class Organization(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Settings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    total = models.IntegerField(default=1)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    burger = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.phone
