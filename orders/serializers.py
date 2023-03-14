from rest_framework import serializers

from orders.models import Order, Customer, Shipping, Item


class CustomerSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Customer
    fields = ("pk","first_name", "last_name", "country", "age")


class OrderSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Order
    fields = ("item", "amount", "customer")


class ShippingSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Shipping
    fields = ("status", "customer")


class ItemSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Item
    fields = ("pk", "name", "total_amount", "slug")