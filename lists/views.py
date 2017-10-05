from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text) # create new Item without needing to call .save()
    return redirect('/lists/the-only-list-in-the-world/')