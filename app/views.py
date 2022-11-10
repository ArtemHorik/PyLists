from django.shortcuts import redirect, render
from .models import Item


def home_page(request):
    """Home page"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect('/lists/unique-list/')
    return render(request, 'home.html')


def view_list(request):
    """List view"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
