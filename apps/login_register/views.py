# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import *


# Create your views here.
def index(request):
    login_form = UserLoginForm(request.POST or None)
    reg_form = UserRegistrationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
        'profile_form': profile_form,
    }
    return render(request, 'login_register/index.html', context)


def to_login(request):
    login_form = UserLoginForm(request.POST or None)
    reg_form = UserRegistrationForm()
    profile_form = ProfileForm()
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
        'profile_form': profile_form,
    }
    if login_form.is_valid():
        """
        " use the following if using EMAIL to sign in
        " email = login_form.cleaned_data.get('email')
        """
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user_model = get_user_model()
        """
        " username = user_model.objects.get(email=email).username
        """
        user = authenticate(username=username, password=password)
        login(request, user)
        # TODO: return redirect('reviews:index')
    return render(request, 'login_register/index.html', context)


def to_logout(request):
    logout(request)
    return redirect('login_register:index')


def to_register(request):
    login_form = UserLoginForm()
    reg_form = UserRegistrationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
        'profile_form': profile_form,
    }
    if reg_form.is_valid() and profile_form.is_valid():
        new_user = reg_form.save(commit=False)
        password = reg_form.cleaned_data.get('password')
        new_user.set_password(password)
        new_user.save()
        # save user profile
        user = get_user_model()
        user_query = user.objects.get(username=new_user.username)
        birthday = profile_form.cleaned_data.get('birthday')
        UserProfile.objects.create(user=user_query, birthday=birthday)
        # auto login after registration
        log_new_user = authenticate(username=new_user.username, password=password)
        login(request, log_new_user)
        # TODO: return redirect('reviews:index')
    return render(request, 'login_register/index.html', context)

