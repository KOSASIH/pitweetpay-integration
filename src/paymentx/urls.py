from django.urls import path
from .paymentx.twitter.views import create_payment_request
from .pi_network.views import pi_network_callback

urlpatterns = [
    path("create_payment_request/", create_payment_request, name="create_payment_request"),
    path("pi_network/callback/", pi_network_callback, name="pi_network_callback"),
]
