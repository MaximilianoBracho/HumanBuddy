from django.urls import path
from SiteAdmin import views

urlpatterns = [
    path('',views.manage),
]