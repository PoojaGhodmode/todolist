from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addtask', views.addtask, name="addtask"),
    path('delete/<int:pk>', views.delete, name="delete"),

]