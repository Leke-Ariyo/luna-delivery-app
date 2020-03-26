from django.db import models
from django.utils.timezone import now
from accounts.models import Profile

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    menu_list = models.ForeignKey('MenuList', on_delete=models.DO_NOTHING,
                                  null=True, blank=True)


class MenuList(models.Model):
    name = models.CharField(max_length=255)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    units = models.IntegerField(default=1)
    menu_list = models.ForeignKey('MenuList', on_delete=models.DO_NOTHING,
                                  null=True, blank=True)


class Order(models.Model):
    payment_method = (
        ('card_payment', 'card_payment'),
        ('pay_on_delivery', 'pay_on_delivery')
    )
    status = (
        ('uncompleted', 'uncompleted'),
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('canceled', 'canceled'),
        ('transit', 'transit'),
        ('completed', 'completed')
    )
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    payment_method = models.CharField(max_length=30, choices=payment_method)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=status)
    total_amount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=now, blank=True)
    delivery_company = models.ForeignKey(
        'DeliveryCompany', on_delete=models.CASCADE)


class DeliveryCompany(models.Model):
    name = models.CharField(max_length=255)
    staff_id = models.PositiveIntegerField(blank=True, null=True)
    staff_name = models.CharField(max_length=255, blank=True, null=True)
