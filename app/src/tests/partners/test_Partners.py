import pytest
form django.urls import reverse


@pytest.mark.django_db
class TestParner():

    def test_partner_create(self, client_logged):
        url = reverse('partner-create')
        response = client_logged.get(url)
        assert response.status_code == 200