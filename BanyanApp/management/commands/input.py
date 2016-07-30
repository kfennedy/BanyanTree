import serial, threading, time
from django.core.management.base import BaseCommand, CommandError
from BanyanApp.models import *
from BanyanApp.views import *
from BanyanApp.helper import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ser = serial.Serial('/dev/cu.usbmodem14131', 9600)

        while True:
            airs = Air.objects.all()
            air = airs[0]
            x = ser.readline()
            if x[:6] == "toggle":
                array = x.split('_')
                pin = array[1]
                print "toggled pin = "+ pin
                light = Light.objects.get(pin=int(pin))
                wanted_state = not(light.state)
                turn_smart_lights(light.room, wanted_state)
            elif x=="add\r\n":
                air.value +=1
                air.save()
                print "adding temp"
            elif x=="sub\r\n":
                air.value -=1
                air.save()
                print "subtracting temp"
            else:
                print "COMING FROM ARDUINO: ", x
