from rest_framework import serializers
from .models import StockInfo

class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = ['name', 'date', 'open', 'high', 'low', 'close']