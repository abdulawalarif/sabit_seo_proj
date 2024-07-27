from django import forms

class LocationForm(forms.Form):
    lat_lon = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter latitude,longitude (e.g., 23.88826,90.39065)'})
    )
    radius = forms.FloatField(
        label='Radius in Km',
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter radius in kilometers'})
    )
    total_locations = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter total number of locations'})
    )
