from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^admin/', admin.site.urls),
url('', include("BanyanApp.urls")),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

admin.site.site_header = 'BanyanTree Administration'
