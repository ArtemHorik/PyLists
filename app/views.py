from django.shortcuts import redirect, render
from .models import Item


def home_page(request):
    """Home page"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
