from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def admission_view(request):
    return render(request, 'admission.html')

def placement_view(request):
    return render(request, 'placement.html')

def events_view(request):
    return render(request, 'events.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def contact_view(request):
    return render(request, 'contact.html')