import serial, threading, time
from django.core.management.base import BaseCommand, CommandError
from BanyanApp.models import *
from BanyanApp.views import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ser = serial.Serial('/dev/cu.usbmodem14211', 9600)

        while True:
            airs = Air.objects.all()
            air = airs[0]
            db = str(air.value)

            x = ser.readline()
            if x=="air\r\n":
                aha = bytes(db)
                ser.write(aha)
                print "sending temp = ",db
                # ser.flush()
            else:
                print "COMING FROM ARDUINO: ", x
