# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=11)
    lastname = models.CharField(max_length=255)
    logdate = models.DateTimeField()

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
