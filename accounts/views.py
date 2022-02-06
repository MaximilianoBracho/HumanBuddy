from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login


def UserRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Daddy')
            user.groups.add(group)
            group = Group.objects.get(name='User')
            user.groups.add(group)
            
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            
            return redirect('Alta de Padre')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
