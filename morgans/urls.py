"""
URL configuration for morgans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from morgans.views import index
from morgans.views import menu
from morgans.views import sucursales
from morgans.views import nosotros
from morgans.views import unete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('unete/', views.unete, name='unete'),
    path("accounts/", include("django.contrib.auth.urls")),
]

#from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#    # Otras rutas de tu aplicación...
#]
