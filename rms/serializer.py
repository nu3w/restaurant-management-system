from rest_framework import serializers
from .models import *

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id','name']
        # exclude = ['name'] 
    
# ---------------------------------------------------------------------------------

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
    
#     def create(self, validated_data):
#         category = Category.objects.create(name = validated_data.get('name'))
#         return category
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance
    
# class TableSerializer(serializers.Serializer):
#     number = serializers.IntegerField()
#     capacity = serializers.IntegerField()
#     is_available = serializers.BooleanField()
    
#     def create(self, validated_data):
#         table = Table.objects.create(
#             number = validated_data.get('number'),
#             capacity = validated_data.get('capacity'),
#             is_available = validated_data.get('is_available'))
#         return table
    
#     def update(self, instance, validated_data):
#         instance.number = validated_data.get('number', instance.number)
#         instance.capacity = validated_data.get('capacity', instance.capacity)
#         instance.is_available = validated_data.get('is_available', instance.is_available)
#         instance.save()
#         return instance