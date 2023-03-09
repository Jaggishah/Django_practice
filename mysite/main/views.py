from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Item,ToDOList
from .forms import CreateNewList
def index(response,id):
    ls = ToDOList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return render(response,'main/base.html',{"name":ls.name})
 
def home(response,id):
    ls = ToDOList.objects.get(id=id)
    return render(response,'main/list.html',{"ls":ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDOList(name=n)
            t.save()
    else:        
        form = CreateNewList()
    return render(response,'main/create.html',{"form":form})