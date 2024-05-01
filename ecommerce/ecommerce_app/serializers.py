from rest_framework import serializers
from .models import *

# serializers are used to render python data types as json or xml content types

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'