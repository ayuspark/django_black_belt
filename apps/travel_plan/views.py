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
    plans = request.user.plans.all()
    joined_plans = request.user.joined_plans.all()
    other_plans = TravelPlan.objects.exclude(creator=request.user).exclude(join=request.user).order_by('start_date')
    context = {
        'plans': plans,
        'joined_plans': joined_plans,
        'other_plans': other_plans,
    }
    return render(request, 'travel_plan/index.html', context)


@login_required(login_url='/')
def join(request, plan_id):
    #get the travel plan to join
    travel_plan = TravelPlan.objects.get(pk=plan_id)
    user = request.user
    user.joined_plans.add(travel_plan)
    return redirect('travel_plan:index')


@login_required(login_url='/')
def add(request):
    form = TravelPlanForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        new_plan = form.save(commit=False)
        new_plan.creator = request.user
        new_plan.save()
        return redirect('travel_plan:index')
    return render(request, 'travel_plan/add.html', context)


def plan_destination(request, plan_id):
    plan = TravelPlan.objects.get(pk=plan_id)
    return render(request, 'travel_plan/destination.html', {'plan': plan,})

