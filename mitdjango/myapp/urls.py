
from django.urls import path
from myapp import views

urlpatterns = [

    path('',views.home,name='home'),

    path('contact/',views.contact,name='contact'),

    path('about/',views.about,name='about_us'),

    path('gallery/',views.gallery,name='gallery'),

    path('services/',views.services,name='services'),

]