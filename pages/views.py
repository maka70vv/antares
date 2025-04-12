from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import DocumentFusitek

def index(request):
    return render(request, 'index.html')

def page_not_found_view(request, exception):
    return render(request, "404.html", status=404)

def fusitek(request):
    return render(request, 'fusitek.html')

def sinikon(request):
    return render(request, 'sinikon.html')

def sinikon_standart(request):
    return render(request, 'sinikon_standart.html')

def sinikon_comfort(request):
    return render(request, 'sinikon_comfort.html')

def sinikon_rain_flow(request):
    return render(request, 'sinikon_rain_flow.html')

def sinikon_universal(request):
    return render(request, 'sinikon.html')

def download_document_fusitek(request, doc_type):
    document = get_object_or_404(DocumentFusitek, doc_type=doc_type)
    return FileResponse(document.file.open('rb'), as_attachment=True, filename=document.file.name)