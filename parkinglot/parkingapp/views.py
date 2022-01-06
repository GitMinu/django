import datetime
from pdb import set_trace
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

def home_page(request):
    return HttpResponse("welcome to the parking lot")


def parking_entry(request):
    if request.method == 'GET':
        form = VehicleDetailsEntryForm()
        context = {'name': 'raja singh', 'form': form}
        return render(request, 'parking.html', context)
    else:
        data = request.POST.copy()
        slot = Parkingslot.get_available_slot(data.get('vehicle_type'))
        # import pdb
        # pdb.set_trace()
        VehicleDetails.objects.create(vehicle_no=data.get('vehicle_no'),
        vehicle_type=data.get('vehicle_type'), slot=slot)
        slot.is_occupied = True
        slot.save()
        return HttpResponse('you are alloted slot no {} and your starttime is {}'.format(slot.slot_no, datetime.datetime.now()))


def parking_exit(request):
    if request.method=="GET":
        form=VehicleDetailsExitForm()
        context = {'name': 'raja singh', 'form': form}
        return render(request, 'parking_exit.html', context)
    else:
        data=request.POST.copy()
        # slot=Parkingslot.get_leaving_slot(data.get('vehicle_type'))        
        veh = VehicleDetails.objects.get(vehicle_no=data.get('vehicle_no'))
        slot = veh.slot
        slot.is_occupied = False
        slot.save()
        return HttpResponse('The vehicle slot is vacated for vehicle {} and slot {}'.format(veh.vehicle_no, slot.slot_no))
        



