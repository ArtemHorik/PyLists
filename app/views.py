from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from app.forms import ItemForm
from app.models import Item, List


def home_page(request):
    """Home page"""
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    """List view"""
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
        else:
            return render(request, 'list.html', {'form': form})
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    """Creates new list"""
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST.get('text'), list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
