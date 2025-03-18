from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('fusitek/', fusitek, name='fusitek'),
    path("download_fusitek/<str:doc_type>/", download_document_fusitek, name="download_document_fusitek"),
]
