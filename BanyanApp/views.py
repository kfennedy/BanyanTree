import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
# from arduinoMorse import ArduinoMorse

from .forms import *
from BanyanApp.models import *
from BanyanApp.helper import *

import serial, threading, time
import tkMessageBox
from django.core.management.base import BaseCommand, CommandError

def root(request):
    return render(request, "root.html")

def home(request):
    lights = Light.objects.all()
    airs = Air.objects.all()
    context = {"dict": {"lights":lights}}

    if request.method == 'POST':
        if "lights" in request.POST:
            room = request.POST.get("room")
            state = clean(request.POST.get("state"))
            light = Light.objects.get(room=room)
            light.state = state
            light.save()

        elif "all_lights" in request.POST:
            state = request.POST.get("all_lights")
            state = bool(state)
            for light in lights:
                light.state = state
                light.save()

        elif "all_airs" in request.POST:
            state = request.POST.get("all_airs")
            state = bool(state)
            for air in airs:
                air.state = state
                air.save()


    return render(request, "home.html", context)
