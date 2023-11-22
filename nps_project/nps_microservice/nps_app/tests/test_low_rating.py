from rest_framework import status
from rest_framework.test import APITestCase
from nps_app.domain import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class CompanyViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@test.co", password="testpassword", name="testuser"
        )
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_low_rating(self):
        url = "/api/1.0/low_rating/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
