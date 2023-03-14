from django.db import models

# Create your models here.


class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  age = models.PositiveSmallIntegerField()

  def __str__(self):
    return f"{self.first_name}|{self.last_name}"
    


class Order(models.Model):
  amount = models.PositiveSmallIntegerField()
  item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="items")  
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                               related_name="customers")

  def __str__(self):
    return f"{self.customer.first_name}|{self.item.name}"
  


class Shipping(models.Model):
  
  PENDING = 0
  DELIVERED = 1

  STATUSES = ((PENDING, "Pending"),
              (DELIVERED, "Delivered"),)

  status = models.PositiveSmallIntegerField(choices=STATUSES)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                               related_name="customers_from_shipping")

  def __str__(self):
    return f"{self.customer.first_name}|{self.status}"

  
class Item(models.Model):
  name = models.CharField(max_length=100)
  total_amount = models.IntegerField()
  slug = models.SlugField(max_length=100, unique=True)

  def __str__(self):
    return f"{self.name}|{self.total_amount}"
  
  