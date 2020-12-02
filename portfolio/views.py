from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.


def home(requst):
    projects = Project.objects.all()
    return render(requst, 'portfolio/home.html', {'projects':projects})