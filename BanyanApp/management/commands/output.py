import serial, threading, time
from django.core.management.base import BaseCommand, CommandError
from BanyanApp.models import *
from BanyanApp.views import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

        while True:
            lights = Light.objects.all()
            db = ""

            # constructing db state (pin,state)
            # 2 False 4 False 6 False 8 False 10 False 12 False
            for light in lights:
                pin = str(light.pin)
                state = str(0) if light.state is False else str(1)
                db += pin
                db += " "
                db += state
                db += " "
            db += " "

            x = ser.readline()

            if x == "output\r\n":
                print "db = ", db
                aha = bytes(db)
                ser.write(aha)
            else:
                print "COMING FROM ARDUINO: ", x
