from django.shortcuts import render
from django.http import HttpResponse
from .models import People
import requests
import json

def index(request):
    Persons = People.objects
    print(Persons.all()[0].name)
    return HttpResponse('hello world')



def other(request):
    Persons = People.objects
    return render(request, 'people/other.html', {'people':Persons.all()})

def thirdpartyapi(request):
    import requests
    import json
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,TRX&tsyms=USD")
    print(price_request.content)
    price = price_request.json()

    return render(request, 'people/price.html', {'price':price})

# Create your views here.
