from django.urls import path
from home import HomeTV


urlpatterns = [
    path('', HomeTV.as_view(), name='home'),
]