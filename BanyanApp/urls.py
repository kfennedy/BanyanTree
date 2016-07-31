from django.conf.urls import url, include
from django.contrib import admin

from .views import (
root, configA, indiv
)


urlpatterns = [
url(r'^$', root),
url(r'^configA/$', configA),
url(r'^indiv/$', indiv),
]
