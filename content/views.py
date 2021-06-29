from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=92e355e9126abf9ca9ac2a472f2348d6'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    return render(request, 'content/index.html') #returns the index.html template