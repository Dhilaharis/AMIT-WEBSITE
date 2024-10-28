from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def business_page(request):
    return render(request, 'business.html')

def projects_page(request):
    return render(request, 'projects.html')

def products_page(request):
    return render(request, 'products.html')

def training_page(request):
    return render(request, 'training.html')

def contact_page(request):
    return render(request, 'contactus.html')