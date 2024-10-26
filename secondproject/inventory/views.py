from django.shortcuts import render


def index(request):
    return render(request, 'djangoapp/index.html')

# Create your views here.
