from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Homepage view that displays a simple HTML page
    """
    return render(request, 'home.html') 