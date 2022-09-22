from django.db import models
from datetime import date, timezone

# Create your models here.
class Customers(models.Model):
    customer_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50)
    #date = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    departament = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=10, blank=True)
    #active = models.BooleanField(default=True)
class Bike(models.Model):
    bike_id =  models.AutoField(primary_key=True)
    bike_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    bike_category = models.CharField(max_length=25)
    country = models.CharField(max_length=25, blank=True)
    bike_image = models.CharField(max_length=150)
    brand = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    size_rin = models.CharField(max_length=3, blank=True)
    size_frame = models.CharField(max_length=3, blank=True)
    brake_system = models.CharField(max_length=25)
    year = models.DateField(null=True, blank=True)
    bike_price = models.DecimalField(max_digits=20, decimal_places=2)    
    stock = models.SmallIntegerField(default=1)
    created_at = models.DateField(default=date.today, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #Order
class Order(models.Model):
    id_cust_order = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customers, related_name='customer_order', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    fecha = models.DateField()
   
#OrderItem
class OrderProduct(models.Model):
    customer_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Bike, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.SmallIntegerField(default=1)