class PaymentXError(Exception):
    """Base exception for all PaymentX exceptions."""
    pass

class PaymentXAPIError(PaymentXError):
    """Exception raised when there is an error with the PaymentX API."""
    def __init__(self, status_code, error_code, error_message):
        self.status_code = status_code
        self.error_code = error_code
        self.error_message = error_message

class PaymentXValidationError(PaymentXError):
    """Exception raised when there is a validation error with the PaymentX API."""
    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message
