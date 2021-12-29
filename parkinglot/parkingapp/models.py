from typing import TYPE_CHECKING
from django.db import models

# Create your models here.

class ParkingLot(models.Model):
    no_of_car_slots = models.IntegerField()
    no_of_bike_slots = models.IntegerField()

    class Meta:
        db_table = 'parking_lot'

class Parkingslot(models.Model):
    TYPE_CHOICES = [('car', 'Car'), ('bike', 'Bike')]
    slot_no = models.IntegerField()
    slot_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    is_occupied = models.BooleanField(default=False)

    class Meta:
        db_table = 'parking_slot'

class VehicleDetails(models.Model):
    TYPE_CHOICES = [('car', 'Car'), ('bike', 'Bike')]
    vehicle_no = models.CharField(max_length=10)
    vehicle_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    start_tume = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    slot = models.ForeignKey(Parkingslot, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'vehicle_details'
