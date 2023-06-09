from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products': products})


def navbar(request):
    return render(request, 'navbar.html')

def pizza (request):
     products = Product.objects.all()
     return render(request, 'pizza.html', {'products': products})

def sides(request):
    products = Product.objects.all()
    return render(request, 'sides.html', {'products': products})

def dessert(request):
    products = Product.objects.all()
    return render(request, 'dessert.html', {'products': products})

def localgoods(request):
    localgoods = LocalGoods.objects.all()
    return render(request, 'localgood.html', {'localgoods': localgoods})

def tgtb(request):
    products = Product.objects.all()
    return render(request, 'tgtb.html', {'products': products})

def mistake(request):
    products = Product.objects.all()
    return render(request, 'mistake.html', {'products': products})
