from django.conf.urls import url, include
from django.contrib import admin

from .views import (
root, test, indiv
)


urlpatterns = [
url(r'^$', root),
url(r'^test/$', test),
url(r'^indiv/$', indiv),
]
