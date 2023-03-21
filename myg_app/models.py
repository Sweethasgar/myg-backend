from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media',blank=True)
    price=models.IntegerField(default=0)       

    def __str__(self):
        return self.name

class Review(models.Model):
    user=models.CharField(max_length=150)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='review')
    Review=models.CharField(max_length=150)
    rating=models.FloatField(validators=[MinValueValidator(1),MinValueValidator(5)])      

    def __str__(self):
        return self.Review 


class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    qty = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])
    options = (
        ("in cart", "in cart"),
        ("order_placed", "order_placed"),
        ("cancelled", "cancelled"),

    )
    status = models.CharField(max_length=12, choices=options, default="in cart")     


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderdate = models.DateField(auto_now_add=True, null=True)
    expected_date=models.CharField(max_length=150)
    options = (
        ("order_placed", "order_placed"),
        ("delivered", "delivered")
    )
    status = models.CharField(max_length=20, choices=options, default="order_placed")
        