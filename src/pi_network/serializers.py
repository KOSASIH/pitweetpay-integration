# pi_network/serializers.py
from rest_framework import serializers
from .models import User, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class TransactionSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'created_at']
