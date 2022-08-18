from django.db import models
from django.db.models import SET_NULL, CASCADE
from django.utils.timezone import now


# Create your models here.

class Proprietary(models.Model):
    nif = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=255)
    surnames = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)


class Truck(models.Model):
    register_number = models.CharField(max_length=14, primary_key=True)
    license_plate = models.CharField(max_length=7, null=False)
    brand = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)
    buy_date = models.DateField()
    build_date = models.DateField(null=False)
    kilometers = models.PositiveIntegerField(null=False)
    proprietary = models.ForeignKey(Proprietary, on_delete=SET_NULL, null=True)
    tara = models.PositiveIntegerField(null=False)
    max_auth_load = models.PositiveIntegerField(null=False)
    wheel_number = models.PositiveIntegerField(null=False)


class Van(models.Model):
    register_number = models.CharField(max_length=14, primary_key=True)
    license_plate = models.CharField(max_length=7, null=False)
    brand = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)
    buy_date = models.DateField()
    build_date = models.DateField(null=False)
    kilometers = models.PositiveIntegerField(null=False)
    proprietary = models.ForeignKey(Proprietary, on_delete=SET_NULL, null=True)
    load_volume = models.PositiveIntegerField(null=False)
    load_length = models.PositiveIntegerField(null=False)


class Bus(models.Model):
    register_number = models.CharField(max_length=14, primary_key=True)
    license_plate = models.CharField(max_length=7, null=False)
    brand = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)
    buy_date = models.DateField()
    build_date = models.DateField(null=False)
    kilometers = models.PositiveIntegerField(null=False)
    proprietary = models.ForeignKey(Proprietary, on_delete=SET_NULL, null=True)
    passenger_number = models.PositiveIntegerField(null=False)
    video = models.BooleanField(null=False, default=False)
    wheel_number = models.PositiveIntegerField(null=False)


class Maintenance(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    maintenance_date = models.DateField(null=False, default=now())
    done_work = models.TextField(null=False)
    price = models.FloatField(null=False)
    bus = models.ForeignKey(Bus, on_delete=CASCADE)
    truck = models.ForeignKey(Truck, on_delete=CASCADE)
    van = models.ForeignKey(Van, on_delete=CASCADE)
