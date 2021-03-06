
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)

    admin.site.site_header = "InoBooks Admin"
    admin.site.site_title = "InoBooks Admin Portal"
    admin.site.index_title = "Welcome to InoBooks"