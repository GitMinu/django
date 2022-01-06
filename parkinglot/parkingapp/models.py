from typing import TYPE_CHECKING
from django.db import models, IntegrityError
from django.conf import settings

# Create your models here.

# class ParkingLot(models.Model):
#     no_of_car_slots = models.IntegerField()
#     no_of_bike_slots = models.IntegerField()

#     class Meta:
#         db_table = 'parking_lot'

class Parkingslot(models.Model):
    TYPE_CHOICES = [('car', 'Car'), ('bike', 'Bike')]
    slot_no = models.IntegerField()
    slot_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    is_occupied = models.BooleanField(default=False)

    @classmethod
    def get_available_slot(cls, vehicle_type):
        try:
            slots = cls.objects.filter(is_occupied=False, slot_type=vehicle_type)
            if slots:
                return slots[0]                
            else:
                raise Exception
        except Exception as ex:
            range_of_slots = settings.SLOTS
            for i in range(1, range_of_slots[vehicle_type]+1):
                slot_object, is_created = cls.objects.get_or_create(slot_no=i, slot_type=vehicle_type)
                if slot_object.is_occupied:
                    continue
                return slot_object
    class Meta:
        db_table = 'parking_slot'
        unique_together = ['slot_no', 'slot_type']

    

class VehicleDetails(models.Model):
    TYPE_CHOICES = [('car', 'Car'), ('bike', 'Bike')]
    vehicle_no = models.CharField(max_length=10)
    vehicle_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True,null=True)
    slot = models.ForeignKey(Parkingslot, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'vehicle_details'
