from django.urls import path
from MyVet import views

urlpatterns = [
    path('',views.manage),
]