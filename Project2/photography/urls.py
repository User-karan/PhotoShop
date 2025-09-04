from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("competition/",views.competition,name="competition"),
    path('membership/',views.membership,name="membership"),
]
