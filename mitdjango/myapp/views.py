from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render (request, 'contact.html')

def about(request):
    return render(request, 'about_us.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')


