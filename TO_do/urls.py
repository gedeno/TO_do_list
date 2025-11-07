from django.urls import path
from . import views

urlpatterns = [
    path("",views.taxi, name="taxi" ),

]