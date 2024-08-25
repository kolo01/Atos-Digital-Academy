from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "users/index.html")

def edit(request):
    return render(request, "users/edit.html")

def add(request):
    return render(request, "users/add.html")
    

