from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models  import *
from .serializer import *
# Create your views here.

# function based api
@api_view()
def category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view()
def table(request):
    table = Table.objects.all()
    serializer = TableSerializer(table, many=True)
    return Response(serializer.data)