from django.urls import path
from pages import HomeTV, salesTV


urlpatterns = [
    path('', HomeTV.as_view(), name='home'),
    path('sales/', salesTV.as_view(), name='invoice'),
    
]