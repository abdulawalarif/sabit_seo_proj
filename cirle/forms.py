# forms.py
from django import forms

class LocationForm(forms.Form):
    latitude = forms.FloatField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter latitude'})
    )
    longitude = forms.FloatField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter longitude'})
    )
    radius = forms.FloatField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter radius in kilometers'})
    )
    total_locations = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter total number of locations'})
    )
