from django.urls import path
from MyDaddy import views

urlpatterns = [
    path('',views.manage),
]