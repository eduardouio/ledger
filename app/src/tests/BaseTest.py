import random

import pytest
from accounts.models import CustomUserModel as UserModel
from rest_framework.test import APIClient


class BaseTest():
    """
    This class serves as the base test class for API tests.
    """

    @pytest.fixture
    def client_logged(self, client):
        self.user.role = random.choice(['student', 'teacher', 'school'])
        self.user.save()
        client.force_login(self.user)
        return client

    @pytest.fixture
    def client_guest(self, client):
        self.user.role = 'guest'
        self.user.save()
        client.force_login(self.user)
        return client

    def setup_method(self):
        self.user = UserModel(
            email='test@example.com',
            password='<PASSWORD>.123',
        )

    def test_not_authorized(self, client_guest, url):
        message = 'Su Perfil No tiene permiso para realizar esta acción'
        response = client_guest.get(url)
        assert response.status_code == 403
        response = response.json()
        assert response['detail'] == message

    def test_dont_logged_in_user(self, url):
        message = 'Las credenciales de autenticación no se proveyeron.'
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 403
        response = response.json()
        assert response['detail'] == message