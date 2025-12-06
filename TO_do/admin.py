from django.contrib import admin
from .models import ToDolist,item
# Register your models here.
admin.site.register(ToDolist)
admin.site.register(item)