from django.forms import ModelForm

from .models import VehicleDetails

class VehicleDetailsEntryForm(ModelForm):
    class Meta:
        model = VehicleDetails
        fields = ['vehicle_no', 'vehicle_type']

class VehicleDetailsExitForm(ModelForm):
    class Meta:
        model = VehicleDetails
        fields = ['vehicle_no']