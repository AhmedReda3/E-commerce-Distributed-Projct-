from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 'address',
            'zipcode', 'place', 'phone', 'created_at', 'paid', 'paid_amount',
            'status', 'get_total_price',
        ]

    def get_total_price(self, obj):
        if obj.paid_amount:
            return obj.paid_amount / 100
        return 0
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity', 'get_total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()