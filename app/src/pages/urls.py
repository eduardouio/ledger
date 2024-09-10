from django.urls import path
from pages import HomeTV


urlpatterns = [
    path('', HomeTV.as_view(), name='home'),
]