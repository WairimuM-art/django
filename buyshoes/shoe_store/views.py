from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index1.html')
def about(request):
    return render(request, 'about_us.html')
