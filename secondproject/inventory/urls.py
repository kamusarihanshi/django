from django.urls import path
from . import views

# Define the URL patterns for the 'inventory' app.
urlpatterns = [
    path('', views.index, name='home'),
   
]
