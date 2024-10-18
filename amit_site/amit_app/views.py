from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'index.html')