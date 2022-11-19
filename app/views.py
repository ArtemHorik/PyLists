
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from .models import Item, List


def home_page(request):
    """Home page"""
    return render(request, 'home.html')


def view_list(request, list_id):
    """List view"""
    list_ = List.objects.get(id=list_id)
    item = None
    error = None

    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST.get('item_text'), list=list_)
            item.full_clean()
            item.save()
            return redirect(f'/lists/{list_.id}/')
        except ValidationError:
            item.delete()
            error = "You can't have an empty list item'"
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    """Creates new list"""
    list_ = List.objects.create()
    item = Item(text=request.POST.get('item_text'), list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect(f'/lists/{list_.id}/')
