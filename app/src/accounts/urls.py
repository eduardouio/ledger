from django.urls import path
from accounts.views import LoginTV

app_name = "accounts"
urlpatterns = [
    path('accounts/login/', LoginTV.as_view(), name='login'),
    #path('accounts/logout/', LogoutRV.as_view(), name='logout'),
]