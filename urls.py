"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CCS import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name="base"),
    path('signin/',views.signin,name="signin"),
    path('loginerror/',views.loginerror,name="loginerror"),
    path('uploadhtml/',views.uploadhtml,name="uploadhtml"),
    path('exportcsv', views.exportcsv),
    path('showlogin/',views.showlogin,name="show"),
    path('showdocument/',views.showdocument,name="showdocument"),
    path('faclogin/',views.faclogin,name="faclogin"),
    path('facerror/',views.facerror,name="facerror"),
    path('facdata/',views.facdata,name="facdata"),
    path('base1/',views.base1,name="base1"),
    path('fac_data_fail/',views.fac_data_fail,name="fac_data_fail"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)