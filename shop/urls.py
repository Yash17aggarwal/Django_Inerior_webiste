from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home ,name='index'),
    path('About us',views.about,name='About us'),
    path('contact',views.Contac,name='contact'),
    path('Home',views.Home,name='home'),
    path('Bedroom',views.Bedroom,name='bed'),
    path('Kitchen', views.Kitchen, name='kit'),
    path('Hall', views.Hall, name='Hall'),
    path('Subscribe',views.sub,name='subscribe')

]