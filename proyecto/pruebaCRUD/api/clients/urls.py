from django.urls import path
from . import views

app_name = 'clientsAPI'

urlpatterns = [
    path('get/', views.get, name='get'),
    path('createOrUpdate/', views.createOrUpdate, name='createOrUpdate'),
    path('delete/<int:client_id>', views.delete, name='delete')
]