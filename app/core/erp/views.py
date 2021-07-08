from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from core.erp.models import Category, Product


def index(request):
    data = {
        'categories': Category.objects.all()
    }
    return render(request, "index.html", data)


def segunda_vista(request):
    data = {
        'products': Product.objects.all()
    }
    return render(request, "second_view.html", data)
