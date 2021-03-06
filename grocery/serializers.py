from rest_framework import serializers
from .models import GroceryItem

class GrocerySerializer(serializers.ModelSerializer):

    class Meta:
        model = GroceryItem
        fields = ('id','name','quantity','price','created_date', 'total',)