from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """Home page"""
    return HttpResponse('<html><title>To-Do lists</title></html>', content_type='text/html')
