from django.contrib import admin
from orders.models import Order, SubOrder, GiftCode, Basket, Book

admin.site.register(Order)
admin.site.register(SubOrder)
admin.site.register(GiftCode)
admin.site.register(Basket)
admin.site.register(Book)
