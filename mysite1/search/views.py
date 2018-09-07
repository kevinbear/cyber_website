from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def search_product(request, product):
    return HttpResponse(str(product))
    # return render(request, 'home.html')


def search_shop(request):
    return render(request, 'home.html')


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
