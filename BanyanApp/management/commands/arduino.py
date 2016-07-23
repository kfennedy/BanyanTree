import serial, threading, time
import tkMessageBox
from django.core.management.base import BaseCommand, CommandError
from BanyanApp.models import *
from BanyanApp.views import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def construct(self, list):
        output = ""
        for i in list:
            output += i
            output += " "
        output += " "
        return output

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

            # print "dbDATA = ", db

            # light1 = lights[0]
            # light2 = lights[1]
            # light3 = lights[2]
            # light4 = lights[3]
            # light5 = lights[4]
            #
            # led_pin1 = str(light1.pin)
            # state1 = str(0) if light1.state is False else str(1)
            # led_pin2 = str(light2.pin)
            # state2 = str(0) if light2.state is False else str(1)
            # led_pin3 = str(light3.pin)
            # state3 = str(0) if light3.state is False else str(1)
            # led_pin4 = str(light4.pin)
            # state4 = str(0) if light4.state is False else str(1)
            # led_pin5 = str(light5.pin)
            # state5 = str(0) if light5.state is False else str(1)
            #
            # dbData = self.construct([led_pin1,state1])
            # dbData = self.construct([led_pin1,state1,led_pin2,state2,led_pin3,state3,led_pin4,state4,led_pin5,state5])
            # print " dbData = ", dbData
            # print "length of dbData = ", len(dbData)


            x = ser.readline()

            if x == "r\r\n":
                # aha = bytes(dbData)
                # print  " are you here?"
                aha = bytes(db)
                ser.write(aha)
            elif x[:8] == "toggleON":
                print x
                array = x.split('_')
                pin = array[1]
                light = Light.objects.get(pin=int(pin))
                light.state = True
                light.save()
            elif x[:9] == "toggleOFF":
                print x
                array = x.split('_')
                pin = array[1]
                light = Light.objects.get(pin=pin)
                light.state = False
                light.savec
            else:
                print "COMING FROM ARDUINO: " , x
        ser.close()
