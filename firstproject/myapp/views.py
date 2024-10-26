from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour


def home(request):
    tours=Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tour/index.html', context)

# Create your views here.
