from django.contrib import admin
from .models import *


@admin.register(DocumentFusitek)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("doc_type", "uploaded_at")


