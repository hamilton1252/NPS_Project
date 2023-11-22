from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from unittest.mock import patch
from nps_app.decorators import log_event


@log_event
def test_function(self, request):
    return HttpResponse("Test response")


# Clase de prueba para el decorador log_event
class LogEventDecoratorTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("nps_app.decorators.logger")
    def test_log_event_decorator(self, mock_logger):
        request = self.factory.get(
            "/path",
            HTTP_USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        )

        response = test_function(self, request)

        self.assertEqual(response.status_code, 200)
        mock_logger.info.assert_called_with(
            "Browser: Firefox, OS: Windows, Device: Other"
        )
