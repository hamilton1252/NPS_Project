from rest_framework import status
from rest_framework.test import APITestCase
from nps_app.domain import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class ReportTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@test.co", password="testpassword", name="testuser"
        )
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_report_top_retractor(self):
        url = "/api/1.0/report_detractor/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_report_top_promoter(self):
        url = "/api/1.0/report_promoter/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_report_report_monthly(self):
        url = "/api/1.0/report_monthly/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
