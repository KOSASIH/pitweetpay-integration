from rest_framework import serializers
from .models import PaymentRequest, Payment, Transaction

class PaymentRequestSerializer(serializers.ModelSerializer):
    """Serializer for PaymentRequest model."""
    class Meta:
        model = PaymentRequest
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment model."""
    class Meta:
        model = Payment
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for Transaction model."""
    class Meta:
        model = Transaction
        fields = '__all__'
