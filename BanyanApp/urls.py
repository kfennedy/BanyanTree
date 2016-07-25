from django.conf.urls import url, include
from django.contrib import admin

from .views import (
root, home, indiv
)


urlpatterns = [
url(r'^$', root),
url(r'^home/$', home),
url(r'^indiv/$', indiv),
]
