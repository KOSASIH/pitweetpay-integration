import requests
from .exceptions import PiNetworkAPIError

class PiNetworkClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.pi-network.com/v1"

    def _request(self, method, url, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        kwargs["headers"] = headers
        response = requests.request(method, url, **kwargs)
        if response.status_code >= 400:
            raise PiNetworkAPIError(response.json())
        return response.json()

    def get_user_balance(self, user_id):
        url = f"{self.base_url}/users/{user_id}/balance"
        return self._request("GET", url)

    # Other Pi Network API methods...
