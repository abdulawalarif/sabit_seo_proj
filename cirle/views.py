from django.shortcuts import render
from .forms import LocationForm
import math

def generate_coordinates(lat, lon, distance_km, num_points=2000):
    R = 6371.0
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    coordinates = []
    for i in range(num_points):
        angle = math.radians(360 / num_points * i)
        new_lat = math.asin(math.sin(lat_rad) * math.cos(distance_km / R) +
                            math.cos(lat_rad) * math.sin(distance_km / R) * math.cos(angle))
        new_lon = lon_rad + math.atan2(math.sin(angle) * math.sin(distance_km / R) * math.cos(lat_rad),
                                       math.cos(distance_km / R) - math.sin(lat_rad) * math.sin(new_lat))
        new_lat_deg = math.degrees(new_lat)
        new_lon_deg = math.degrees(new_lon)
        coordinates.append((new_lat_deg, new_lon_deg))
    return coordinates

def home(request):
    form = LocationForm()
    data_list = None

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            lat_lon = form.cleaned_data['lat_lon']
            try:
                latitude, longitude = map(float, lat_lon.split(','))
            except ValueError:
                form.add_error('lat_lon', 'Invalid format. Use "latitude,longitude".')
            else:
                radius = form.cleaned_data['radius']
                total_locations = form.cleaned_data['total_locations']
                data_list = generate_coordinates(latitude, longitude, radius, total_locations)

    return render(request, 'index.html', {'form': form, 'data_list': data_list})
