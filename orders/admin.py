from django.contrib import admin

from orders.models import Order, Customer, Shipping, Item

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Shipping)
admin.site.register(Item)
