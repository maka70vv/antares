from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('fusitek/', fusitek, name='fusitek'),
    path('sinikon/', sinikon, name='sinikon'),
    path('sinikon/standart/', sinikon_standart, name='sinikon_standart'),
    path('sinikon/comfort/', sinikon_comfort, name='sinikon_comfort'),
    path('sinikon/rainflow/', sinikon_rain_flow, name='sinikon_rain_flow'),
    path('sinikon/universal/', sinikon_universal, name='sinikon_universal'),
    path("download_fusitek/<str:doc_type>/", download_document_fusitek, name="download_document_fusitek"),
]
