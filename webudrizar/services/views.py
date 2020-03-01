from django.shortcuts import render
from .models import Project

# Create your views here.
def services(request):
    projects = Project.objects.all() # devuelve todos los objetos que tiene el modelo projecto
    return render(request, "services/services.html", {'projects':projects})