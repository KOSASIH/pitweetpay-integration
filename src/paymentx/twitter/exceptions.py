import logging

class PaymentXError(Exception):
    """Base exception class for PaymentX errors"""
    def __init__(self, message, code=None, data=None):
        self.message = message
        self.code = code
        self.data = data
        super().__init__(message)

    def __str__(self):
        return f"PaymentXError: {self.message} (Code: {self.code})"

    def log(self):
        logging.error(f"PaymentXError: {self.message} (Code: {self.code})", extra={"data": self.data})

class PaymentGatewayError(PaymentXError):
    """Error raised when a payment gateway returns an error"""
    def __init__(self, message, code, data, gateway_name):
        super().__init__(message, code, data)
        self.gateway_name = gateway_name

    def __str__(self):
        return f"PaymentGatewayError: {self.message} (Code: {self.code}) on {self.gateway_name}"

class PaymentRequestError(PaymentXError):
    """Error raised when a payment request is invalid or cannot be processed"""
    def __init__(self, message, code, data, payment_request_id):
        super().__init__(message, code, data)
        self.payment_request_id = payment_request_id

    def __str__(self):
        return f"PaymentRequestError: {self.message} (Code: {self.code}) on payment request {self.payment_request_id}"

class TransactionError(PaymentXError):
    """Error raised when a transaction cannot be processed"""
    def __init__(self, message, code, data, transaction_id):
        super().__init__(message, code, data)
        self.transaction_id = transaction_id

    def __str__(self):
        return f"TransactionError: {self.message} (Code: {self.code}) on transaction {self.transaction_id}"
