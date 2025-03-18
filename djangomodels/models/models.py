from django.db import models

# Create your models here.
class Students(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    DOB=models.DateField()

    def __str__(self):
        return self.firstname

# create model class called contact: name, course, timing, mobile number and gender

class Contact(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    timing=models.TimeField()
    mobile_number=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employees(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    id_number=models.CharField(max_length=50)
    time_in=models.TimeField()
    time_out=models.TimeField()
    hours=models.IntegerField()

    def __str__(self):
        return self.first_name

class Login(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.EmailField()
    Password=models.CharField(max_length=50)
    Confirm_password=models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName