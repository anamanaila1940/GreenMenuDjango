
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .mistakeform import MistakeForm
from .localform import LocalGoodsForm
from items.models import *





def navbar(request):
    return render(request, 'nav.html')
def index(request):
    products = Product.objects.all() 
    return render(request,'home.html',{'products': products} )

def update(request, id):
    products = Product.objects.get(id=id) 
    form= ProductForm(instance=products)
    if request.method == 'POST':
        form=ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('/chef')

    context={'form':form}
    return render(request,'updates.html',context )


def mistakes(request):
    products = Product.objects.all()
    return render(request,'success.html', {'products': products})

def createMistake(request, id):
    products = Product.objects.get(id=id) 
    form= MistakeForm(instance=products)
    if request.method == 'POST':
        form=MistakeForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('/chef/mistakes')

    context={'form':form}
    return render(request,'create_mistake.html',context )

def localgoods(request):
    form = LocalGoodsForm()
    if request.method == 'POST':
        form = LocalGoodsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'createlocal.html',context)



