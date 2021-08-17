from django.shortcuts import render
import urllib.request
import json
from datetime import datetime


def home(request):
    if request.method == 'POST':
        city = request.POST['city']

        response = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=87368975a3c584b7886a377dd6376fc6').read()
        data = json.loads(response)
        infos = {
            "temp": str(data['main']['temp']),
            "country_code": str(data['sys']['country']),
            "weather": str(data['weather'][0]['main']),
            "description": str(data['weather'][0]['description']),
            "icon": data['weather'][0]['icon'],
            "pressure": str(data['main']['pressure']),
            "humidity": str(data['main']['humidity']),
            "sunrise": str(datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')),
            "sunset": str(datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')),
            "timezone": str(data['timezone']),

        }
    else:
        infos = {}

    return render(request, "Weather/home.html", {'infos': infos})
