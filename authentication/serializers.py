from rest_framework import serializers
from .models import CustomUser
from order.models import Order


class CustomUserCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active'


class CustomUserOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
