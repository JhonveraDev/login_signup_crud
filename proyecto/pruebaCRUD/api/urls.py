from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('clients/', include('pruebaCRUD.api.clients.urls', namespace="clientsAPI")),
]