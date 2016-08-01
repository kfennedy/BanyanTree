from BanyanApp.models import *

min_temp = 18
max_temp = 32

#return a Python boolean object
def clean(value):
    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        return None

# A, B, or C
selected_conf = None

# A1, B2, B3
selected_mod = None

show = False

# modules and room relationship
modLights ={
"A1": [ "balcony1", "balcony2" ],
"A2": [ "living1", 'living2', "kitchen1", "kitchen2", "bed1", "bed2", "door" ],
"A3": [ "toilet1", "toilet2" ]
}

def turn_smart_lights(room,state):
    for mod, groups in modLights.items():
        for r in groups:
            if r == room:
                module = mod
                for r in modLights[module]:
                    light = Light.objects.get(room=r)
                    light.state = state
                    light.save()
