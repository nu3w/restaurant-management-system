from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models  import *
from .serializer import *
from rest_framework import viewsets
# Create your views here.

# ModelViewSet:
class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    
    def destroy(self, request, pk):
        category = Category.objects.get(pk = pk)
        items = OrderItem.objects.filter(food__category=category).count()
        if items > 0:
            return Response({'detail':'category can not be deleted. Protected in OrderItem'})
        category.delete()
        return Response({'detail':'category deleted successfully'})

# ---------------------------------------------------------------------------------

# Viewset:
# class CategoryViewSet(viewsets.ViewSet):
#     def list(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many = True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# class CategoryDetailViewSet(viewsets.ViewSet):
#     def retrieve(self, request, pk):
#         category = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    
#     def update(self, request, pk):
#         category = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def partial_update(self, request, pk=None):
#         category = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(category, data = request.data, partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def destroy(self, request, pk):
#         category = Category.objects.get(pk = pk)
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({'detail':'category can not be deleted. Protected in OrderItem'})
#         category.delete()
#         return Response({'detail':'category deleted successfully'})

# ---------------------------------------------------------------------------------

# Mixins:
# from rest_framework import generics, mixins
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class CategoryGenericAPIView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
#     def delete(self, request, pk):
#         items = OrderItem.objects.filter(food__category = self.get_object()).count()
#         if items > 0:
#             return Response({"details":"Category can not be deleted. Protected in OrderItem"})
#         self.get_object().delete()
#         return Response({"details":"Category deleted successfully"})

# ---------------------------------------------------------------------------------

# class based: APIView
# from rest_framework.views import APIView

# class CategoryAPIView(APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
    
# class CategoryDetail(APIView):
#     def get(self, request, id):
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data) 
    
#     def post(self, request, id):
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         category = Category.objects.get(id = id)
#         items = OrderItem.objects.filter(food__category = category).count()
#         if items > 0:
#             return Response({"details": "category cannot be deleted"})
#         category.delete()
#         return Response({"detail": "category deleted successfully"})

# ---------------------------------------------------------------------------------

# function based: api_view()
# @api_view(['GET','POST'])
# def category(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# @api_view(['GET','POST',"DELETE"])
# def category_detail(request, id):
#     category = Category.objects.get(id = id)
#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         OrderItem.objects.filter(food__category=category).delete()
#         category.delete()
#         return Response({"detail": "Category deleted successfully"})

# @api_view(['GET','POST'])
# def table(request):
#     if request.method == "GET":
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many = True)      
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = TableSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
    
# @api_view(['GET','POST'])
# def table_detail(request, id):
#     table = Table.objects.get(id = id)
#     if request.method == "GET":
#         serializer = TableSerializer(table)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TableSerializer(table, data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)