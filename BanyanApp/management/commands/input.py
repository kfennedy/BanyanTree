import serial, threading, time
from django.core.management.base import BaseCommand, CommandError
from BanyanApp.models import *
from BanyanApp.views import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

        while True:
            x = ser.readline()
            if x[:6] == "toggle":
                array = x.split('_')
                pin = array[1]
                print "toggled pin = "+ pin
                light = Light.objects.get(pin=int(pin))
                wanted_state = not(light.state)
                light.state = wanted_state
                light.save()
            else:
                print "COMING FROM ARDUINO: ", x
