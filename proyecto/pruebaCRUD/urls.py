from django.contrib import admin
from django.urls import  include, path
from . import views

app_name = 'pruebaCRUD'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('api/', include('pruebaCRUD.api.urls', namespace='api'))
]