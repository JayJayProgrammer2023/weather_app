from django.shortcuts import render

def weather_app(request):
    return render(request, 'weather_app.html')