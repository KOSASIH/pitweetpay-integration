# tests/test_pi_network.py
import unittest
from pi_network.exceptions import PiNetworkError
from pi_network.models import User, Transaction
from pi_network.serializers import UserSerializer, TransactionSerializer

class TestPiNetwork(unittest.TestCase):
    def test_user_serializer(self):
        user = User(name='Alice', email='alice@example.com')
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data, {'id': user.id, 'name': 'Alice', 'email': 'alice@example.com'})

    def test_transaction_serializer(self):
        sender = User.objects.create(name='Alice', email='alice@example.com')
        receiver = User.objects.create(name='Bob', email='bob@example.com')
        transaction = Transaction.objects.create(sender=sender, receiver=receiver, amount=5.0)
        serializer = TransactionSerializer(transaction)
        self.assertEqual(serializer.data, {'id': transaction.id, 'sender': {'id': sender.id, 'name': 'Alice', 'email': 'alice@example.com'}, 'receiver': {'id': receiver.id, 'name': 'Bob', 'email': 'bob@example.com'}, 'amount': 5.0, 'created_at': str(transaction.created_at)})

    def test_pinetwork_error(self):
with self.assertRaises(PiNetworkError):
            raise PiNetworkError('Test PiNetworkError')

if __name__ == '__main__':
    unittest.main()
