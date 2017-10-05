from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    """
    new_item_text: hold the POST contents, or the empty string
    """
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text) # create new Item without needing to call .save()
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})