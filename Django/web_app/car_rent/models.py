from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=11)
    lastname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    rent_id = models.IntegerField()
    mode_payment = models.CharField(max_length=255)
    balance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment'


class Rent(models.Model):
    rent_id = models.AutoField(primary_key=True)
    vehicle_id = models.IntegerField()
    customer_id = models.IntegerField()
    rent_start = models.DateTimeField()
    rent_end = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rent'


class Requirements(models.Model):
    requirements_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    requirement = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'requirements'


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_model = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    plate = models.CharField(max_length=255)
    vehicle_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vehicle'