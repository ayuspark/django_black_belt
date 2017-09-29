# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *


# Create your views here.
def index(request):
    # form = TravelPlanForm(request.POST or None)
    # context = {
    #     'form': form,
    # }
    plans = request.user.plans.all()
    other_plans = TravelPlan.objects.exclude(creator=request.user).order_by('start_date')
    context = {
        'plans': plans,
        'other_plans': other_plans,
    }
    return render(request, 'travel_plan/index.html', context)