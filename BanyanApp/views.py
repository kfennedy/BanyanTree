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

#change this to confA
def test(request):

    lights = Light.objects.all()
    selected_conf = "A"
    show_status = show

    if request.method == 'POST':
        if "lights" in request.POST:
            number = request.POST.get("mod")
            state = clean(request.POST.get("state"))
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
        elif "show" in request.POST:
            show_status = clean(request.POST.get("show"))

    light_status = build_status()
    print "SHOW STATUS = ", show
    context = {"dict": {"lights":lights}, "conf":selected_conf, "show":show_status, "status":light_status}

    return render(request, "test.html", context)

def indiv(request):
    lights = Light.objects.all()
    air = Air.objects.all()[0]
    context = {"dict": {"lights":lights}, "air":air}

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

        elif "air" in request.POST:
            state = request.POST.get("air")
            state = bool(state)
            air.state = state
            air.save()

        elif "air_add" in request.POST:
            air.value += 1
            air.save()

        elif "air_sub" in request.POST:
            air.value -= 1
            air.save()

    return render(request, "indiv.html", context)

# {'A1': False, 'A3': False, 'A2': False}
def build_status():
    modules = modLights.keys()
    status = {}
    for mod in modules:
        status[mod] = Light.objects.get(room=modLights[mod][0]).state
    return status
