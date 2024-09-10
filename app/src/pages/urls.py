from django.urls import path
from pages import HomeTV, InvoiceTV


urlpatterns = [
    path('', HomeTV.as_view(), name='home'),
    path('invoice', InvoiceTV.as_view(), name='invoice'),
]