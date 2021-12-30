import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import VehicleDetailsEntryForm

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

