from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    
class TableSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    capacity = serializers.IntegerField()
    is_available = serializers.BooleanField()