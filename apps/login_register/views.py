# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import *


# Create your views here.
def index(request):
    login_form = UserLoginForm(request.POST or None)
    reg_form = UserRegistrationForm(request.POST or None)
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
    }
    return render(request, 'login_register/index.html', context)


def to_login(request):
    login_form = UserLoginForm(request.POST or None)
    reg_form = UserRegistrationForm()
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user_model = get_user_model()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('travel_plan:index')
    return render(request, 'login_register/index.html', context)


def to_logout(request):
    logout(request)
    return redirect('login_register:index')


def to_register(request):
    login_form = UserLoginForm()
    reg_form = UserRegistrationForm(request.POST or None)
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
    }
    if reg_form.is_valid():
        new_user = reg_form.save(commit=False)
        # get first_name and last_name for User Model
        name = reg_form.cleaned_data.get('name')
        first_name = name.split()[0]
        try:
            last_name = ' '.join(name.split()[1:])
        except:
            last_name = ''
        new_user.first_name = first_name
        new_user.last_name = last_name
        # set user password
        password = reg_form.cleaned_data.get('password')
        new_user.set_password(password)
        new_user.save()
        # auto login after registration
        log_new_user = authenticate(username=new_user.username, password=password)
        login(request, log_new_user)
        return redirect('travel_plan:index')
    return render(request, 'login_register/index.html', context)

