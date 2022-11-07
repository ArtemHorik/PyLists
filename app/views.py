from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """Home page"""
    return render(request, 'home.html')
