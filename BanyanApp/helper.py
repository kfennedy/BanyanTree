from BanyanApp.models import *

#return a Python boolean object
def clean(value):
    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        return None
