# pi_network/exceptions.py
class PiNetworkError(Exception):
    pass

class UserNotFoundError(PiNetworkError):
    pass

class TransactionNotFoundError(PiNetworkError):
    pass
