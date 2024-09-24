from django.urls import path
from pages import HomeTV, salesTV


urlpatterns = [
    path('chateau/', HomeTV.as_view(), name='home'),
    path('ols/', salesTV.as_view(), name='invoice'),
    
]