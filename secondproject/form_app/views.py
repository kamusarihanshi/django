from django.shortcuts import render,redirect
from. forms import ContactForm

# Create your views here.
def homepage (request):
    return render(request, 'form_app/homepage.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect( 'form_app/success.html')
        else:
            return render(request, 'form_app/contact.html', {'form': form})
    
    
    return render(request, 'form_app/contact.html', {'form': form})
    

    


def about (request):
    return render(request, 'form_app/about.html')
def contact (request):
    return render(request, 'form_app/contact.html')

def success (request):
    return render(request, 'form_app/success.html')
