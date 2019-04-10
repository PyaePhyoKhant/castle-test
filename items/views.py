from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from items.forms import ItemForm
from items.models import Item
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def add(request):
    if request.method == 'GET':
        context = {'form': ItemForm}
        return render(request, 'items/add.html', context)
    elif request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
        return redirect('home')


@login_required(login_url='/login/')
def home(request):
    context = {'items': Item.objects.filter(created_by=request.user)}
    return render(request, 'home.html', context)
