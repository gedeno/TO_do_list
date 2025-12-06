from django.shortcuts import render
from  django.http import HttpResponse
from .models import ToDolist, item

def taxi(response,id):
    ls = ToDolist.objects.get(id=id)
    return render(response, "TO_do/base.html", {})

def home(response):
    return render(response, "TO_do/home.html", {})