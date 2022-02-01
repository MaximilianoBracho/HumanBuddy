from django.urls import path
from MyCare import views

urlpatterns = [
    path('',views.manage),
]