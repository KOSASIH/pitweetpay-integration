from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .client import PiNetworkClient
from .exceptions import PiNetworkAPIError

@csrf_exempt
def pi_network_callback(request):
    if request.method != "POST":
        return render(request, "pi_network/callback.html", {"error": "Invalid request method"})

    try:
        pi_network_client = PiNetworkClient(api_key=settings.PI_NETWORK_API_KEY)
        pi_network_user_id = request.POST["user_id"]
        transaction_id = request.POST["transaction_id"]
        amount = float(request.POST["amount"])
        currency = request.POST["currency"]
    except KeyError:
        return render(request, "pi_network/callback.html", {"error": "Missing required parameters"})

    try:
        pi_network_client.confirm_transaction(transaction_id=transaction_id, amount=amount, currency=currency)
        # Update the payment request status in PaymentX
        # ...
    except PiNetworkAPIError as e:
        return render(request, "pi_network/callback.html", {"error": str(e)})

    return render(request, "pi_network/callback.html", {"success": True})
