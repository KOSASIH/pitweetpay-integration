from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .client import PaymentXClient
from .exceptions import PaymentXAPIError

@csrf_exempt
def create_payment_request(request):
    if request.method != "POST":
        return render(request, "paymentx/create_payment_request.html", {"error": "Invalid request method"})

    try:
        amount = float(request.POST["amount"])
        currency = request.POST["currency"]
        description = request.POST["description"]
        pi_network_user_id = request.POST["pi_network_user_id"]
    except KeyError:
        return render(request, "paymentx/create_payment_request.html", {"error": "Missing required parameters"})

    try:
        paymentx_client = PaymentXClient(api_key=settings.PAYMENTX_API_KEY, api_secret_key=settings.PAYMENTX_API_SECRET_KEY)
        payment_request = paymentx_client.create_payment_request(
            amount=amount,
            currency=currency,
            description=description,
            redirect_url=f"{settings.PI_NETWORK_REDIRECT_URL}/{pi_network_user_id}"
        )
    except PaymentXAPIError as e:
        return render(request, "paymentx/create_payment_request.html", {"error": str(e)})

    return render(request, "paymentx/create_payment_request.html", {"payment_request": payment_request})
