from django.shortcuts import render

# pylint: disable=unused-variable
# pylint: enable=too-many-lines

def home(request):
    import json
    import requests

    api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94080&distance=5&API_KEY=FB8713A4-7780-42D7-9B2D-AF57A058FF1B")

    try:
        api = json.loads(api_requests.content)
    except Exception as e:
        api = "Error..."

    #http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=94080&distance=10&API_KEY=FB8713A4-7780-42D7-9B2D-AF57A058FF1B
    
    return render(request, 'home.html', { 'api': api})

def about(request):
    return render(request, 'about.html', {})