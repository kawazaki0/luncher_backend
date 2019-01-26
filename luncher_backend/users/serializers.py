from rest_framework import serializers

from users.models import User
from .models import UserOrder


class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = ('user', 'meal')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
