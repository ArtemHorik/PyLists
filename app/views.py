from django.shortcuts import redirect, render
from .models import Item, List


def home_page(request):
    """Home page"""
    return render(request, 'home.html')


def view_list(request):
    """List view"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    """Creates new list"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text'), list=list_)
    return redirect('/lists/unique-list/')
