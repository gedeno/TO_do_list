from  django.http import HttpResponse

def taxi(request):
    return HttpResponse("Hello, world this my first function .")
def car(request):
    return HttpResponse("Hello, world. this is my scond function.")
def best(request):
    return HttpResponse("Hello, world. this is my third  function.")