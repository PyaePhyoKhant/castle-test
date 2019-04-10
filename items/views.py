from django.http import HttpResponse
from django.shortcuts import render, redirect
from items.forms import ItemForm
from items.models import Item


def add(request):
    if request.method == 'GET':
        context = {'form': ItemForm}
        return render(request, 'items/add.html', context)
    elif request.method == 'POST':
        Item.objects.create(name=request.POST['name'],
                            photo=request.POST['photo'],
                            created_by=request.user)
        return redirect('home')


def home(request):
    context = {'items': Item.objects.filter(created_by=request.user)}
    return render(request, 'home.html', context)
