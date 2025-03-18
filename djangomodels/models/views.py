from django.shortcuts import render,redirect
from .models import Students


#Create your views here

def index(request):
    users=Students.objects.all()
    return render(request, 'index.html', {'users':users})

def addstud(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        DOB = request.POST['DOB']
        query=Students(firstname=firstname, lastname=lastname, email=email, DOB=DOB)
        query.save()
        return redirect('/')
    return render(request,'add_user.html')