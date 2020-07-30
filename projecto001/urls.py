"""projecto001 URL Configuration

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
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LuisAngel, name="index"),
    path('LuisAngel/', views.LuisAngel, name="LuisAngel"),
    path('saludo/', views.saludo, name="saludo"),
    path('rango/',views.rango, name="rango"),
    path('rango2/',views.rango2, name="rango2"),
    path('rango2/<int:a>',views.rango2, name="rango2"),
    path('rango2/<int:a>/<int:b>',views.rango2, name="rango2"),
    path('indexclase13/',views.indexclase13, name="indexclase13"),
    path('foto1/', views.foto1, name="foto1"),
    path('foto2/', views.foto2, name="foto2"),
]

