# tests/test_paymentx.py
import unittest
from paymentx.exceptions import PaymentXError
from paymentx.models import Payment, Transaction
from paymentx.serializers import PaymentSerializer, TransactionSerializer

class TestPaymentX(unittest.TestCase):
    def test_payment_serializer(self):
        payment = Payment(amount=10.0, currency='USD', description='Test Payment')
        serializer = PaymentSerializer(payment)
        self.assertEqual(serializer.data, {'id': payment.id, 'amount': 10.0, 'currency': 'USD', 'description': 'Test Payment'})

    def test_transaction_serializer(self):
        sender = User.objects.create(name='Alice', email='alice@example.com')
        receiver = User.objects.create(name='Bob', email='bob@example.com')
        transaction = Transaction.objects.create(sender=sender, receiver=receiver, amount=5.0)
        serializer = TransactionSerializer(transaction)
        self.assertEqual(serializer.data, {'id': transaction.id, 'sender': {'id': sender.id, 'name': 'Alice', 'email': 'alice@example.com'}, 'receiver': {'id': receiver.id, 'name': 'Bob', 'email': 'bob@example.com'}, 'amount': 5.0, 'created_at': str(transaction.created_at)})

    def test_paymentx_error(self):
        with self.assertRaises(PaymentXError):
            raise PaymentXError('Test PaymentXError')

if __name__ == '__main__':
    unittest.main()
