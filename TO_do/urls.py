from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.taxi, name="taxi"),
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
]