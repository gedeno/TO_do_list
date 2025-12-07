from django.shortcuts import render
from  django.http import HttpResponse
from .models import ToDolist, item
from .forms import CreateNewlist
def taxi(response,id):
    ls = ToDolist.objects.get(id=id)
    return render(response, "TO_do/list.html", {"ls":ls})

def home(response):
    return render(response, "TO_do/home.html", {})
def create(response):
    if response.method == "POST":
        form = CreateNewlist(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDolist(name = n)
            t.save()

    else:
        form =CreateNewlist()
    return render(response, "TO_do/create.html", {"form":form})