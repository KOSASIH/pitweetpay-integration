import requests
from .exceptions import PaymentXAPIError

class PaymentXClient:
    def __init__(self, api_key, api_secret_key):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.base_url = "https://api.paymentx.com/twitter/v1"

    def _request(self, method, url, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "X-PaymentX-Secret-Key": self.api_secret_key,
        }
        kwargs["headers"] = headers
        response = requests.request(method, url, **kwargs)
        if response.status_code >= 400:
            raise PaymentXAPIError(response.json())
        return response.json()

    def create_payment_request(self, amount, currency, description, **kwargs):
        url = f"{self.base_url}/payment_requests"
        data = {
            "amount": amount,
            "currency": currency,
            "description": description,
        }
        data.update(kwargs)
        return self._request("POST", url, json=data)

    # Other PaymentX API methods...
