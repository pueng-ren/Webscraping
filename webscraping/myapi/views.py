from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .webscraping import Webscraping

@api_view(['GET'])
def api_get_symbol(request) :
    if request.method == 'GET' :
        webscraping = Webscraping()
        symbol = webscraping.get_symbol()
        return Response(symbol)

@api_view(['GET'])
def api_get_stock(request, symbol:str) :
    if request.method == 'GET' :
        webscraping = Webscraping()
        stock = webscraping.get_stock(symbol)
    return Response(stock)

    
