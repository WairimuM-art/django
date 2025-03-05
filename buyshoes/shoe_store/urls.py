from django.urls import path
from shoe_store import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='about'),
]
