import os

import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Currency
from .serializers import CurrencySerializer
from .utils import check_existance

load_dotenv()

TOKEN = os.getenv('TOKEN')
ENDPOINT = 'https://currate.ru/api/'


@api_view(['GET'])
def convert(request):
    first_currency = request.GET['from']
    second_currency = request.GET['to']
    amount = float(request.GET['amount'])

    params = {'get': 'rates',
              'pairs': first_currency + second_currency,
              'key': TOKEN}

    response = requests.get(ENDPOINT, params=params)
    response = response.json()

    rate = float(response.get('data')[first_currency + second_currency])

    currency = Currency(name_from=first_currency,
                        name_to=second_currency,
                        amount=amount,
                        value=round((amount * rate), 7))
    serializer = CurrencySerializer(currency)

    return Response(serializer.data)


@api_view(['POST'])
def database(request):
    merge = int(request.GET['merge'])

    serializer = CurrencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    check_existance(serializer.data, merge)
    return Response(serializer.data)
