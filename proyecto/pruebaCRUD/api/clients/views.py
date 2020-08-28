from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
import json

def get(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)

    return JsonResponse({ 'clients': serializer.data}, status=status.HTTP_200_OK)

@csrf_exempt
def createOrUpdate(request):
    json_data = json.loads(request.body)

    if(json_data['id']):
        updateClient(json_data['id'], json_data)

        return JsonResponse({'updated': True})
    else:
        name = json_data['name']
        age = json_data['age']
        address = json_data['address']
        phone = json_data['phone']
        email = json_data['email']
        
        client = Client(name=name, age=age, address=address, phone=phone, email=email)
        client.save()

        return JsonResponse({'id': client.id})

def updateClient(id, json_data):
    client = Client.objects.get(id=id)

    if(client):
        client.name = json_data['name']
        client.age = json_data['age']
        client.address = json_data['address']
        client.phone = json_data['phone']
        client.email = json_data['email']

        client.save()

        return JsonResponse({ 'updated': True })

def delete(request, client_id):
    client = Client.objects.get(id=client_id)

    client.delete()

    return JsonResponse({ 'deleted': True })