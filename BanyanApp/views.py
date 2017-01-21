import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from .forms import *
from BanyanApp.models import *
from BanyanApp.helper import *

import serial, threading, time
import tkMessageBox
from django.core.management.base import BaseCommand, CommandError

def root(request):
    return render(request, "root.html")

def home(request):
    context = {}
    return render(request, "home.html", context)

def configA(request):
    global counter
    lights = Light.objects.all()
    air = Air.objects.all()[0]
    selected_conf = "A"
    show_status = show

    if request.method == 'POST':

        if "lights" in request.POST:
            number = request.POST.get("mod")
            state = clean(request.POST.get("status"))
            if number:
                mod_name = selected_conf + number
                rooms = modLights[mod_name]
                for room in rooms:
                    light = Light.objects.get(room=room)
                    light.state = state
                    light.save()
                    print
            else:
                for light in lights:
                    light.state = state
                    light.save()
            show_status = True

        elif "show" in request.POST:
            show_status = clean(request.POST.get("show"))

        elif "aircon" in request.POST:
            state = clean(request.POST.get("state"))
            air.state = state
            air.save()

        elif "air_add" in request.POST:
            if counter != max_temp:
                air.value += 1
                counter += 1
                air.save()

        elif "air_sub" in request.POST:
            if counter != min_temp:
                air.value -= 1
                counter -= 1
                air.save()

    light_status = build_status()
    context = {"dict": {"lights":lights}, "air":air, "conf":selected_conf, "show":show_status, "status":light_status}

    return render(request, "configA.html", context)

# {'A1': False, 'A3': False, 'A2': False}
def build_status():
    modules = modLights.keys()
    status = {}
    for mod in modules:
        status[mod] = Light.objects.get(room=modLights[mod][0]).state
    return status
