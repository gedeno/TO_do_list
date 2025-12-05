from django.shortcuts import render
from  django.http import HttpResponse
from .models import ToDolist, item

def taxi(request,id):
    ls = ToDolist.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls.name)
