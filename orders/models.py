from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from books.models import Book


class GiftCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    expire_date = models.DateTimeField()
    percent_gift = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_gift', null=True)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_basket')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='temp_purchased')
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    gift = models.ForeignKey(GiftCode, on_delete=models.SET_NULL, related_name='orders_used', null=True)
    total_price = models.IntegerField()
    final_price = models.IntegerField()
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class SubOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='user_orders')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='owner_book')
    price = models.IntegerField()
