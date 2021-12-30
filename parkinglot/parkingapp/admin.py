from django.contrib import admin
from .models import Parkingslot, VehicleDetails

# Register your models here.

# class ParkingLotAdmin(admin.ModelAdmin):
#     pass

class ParkingSlotAdmin(admin.ModelAdmin):
    pass

class VehicleDetailsAdmin(admin.ModelAdmin):
    pass


# admin.site.register(ParkingLot, ParkingLotAdmin)
admin.site.register(Parkingslot, ParkingSlotAdmin)
admin.site.register(VehicleDetails, VehicleDetailsAdmin)
