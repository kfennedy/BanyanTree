import serial, threading, time
from django.core.management.base import BaseCommand, CommandError
from BanyanApp.models import *
from BanyanApp.views import *
from BanyanApp.helper import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ser = serial.Serial('/dev/cu.usbmodem14241', 9600)

        while True:
            x = ser.readline()
            airs = Air.objects.all()
            air = airs[0]
            if x=="add\r\n":
                air.value +=1
                air.save()
                print "adding temp"
            elif x=="sub\r\n":
                air.value -=1
                air.save()
                print "subtracting temp"
            else:
                print "COMING FROM ARDUINO: ", x
