from django.urls import path
from accounts.views import UserRegister


urlpatterns = [
    path('signup/', UserRegister, name='signup'),
]