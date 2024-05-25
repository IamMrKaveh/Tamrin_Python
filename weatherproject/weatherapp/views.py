from django.shortcuts import render
import requests
import datetime


def home(request):
  if request.method =='POST':
    city = ""
    if('city' in request.POST):
      city = request.POST['city']
    else:
      city = "tehran"
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b73aac3355c7221db9fef89f9f47606d'
    params = {'units':'metric'}
    
    data = request.get(url, params).json()
    
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    
    day = datetime.date.today()
    
    
    return render(request, 'weatherapp/home.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})
  
  else:
    return render(request, 'weatherapp/home.html')