from django.core.management import call_command
from django.test import TestCase
from unittest.mock import patch


class LoadAllDataCommandTest(TestCase):
    @patch("nps_app.management.commands.load_country_api.Command.handle")
    @patch("nps_app.management.commands.load_company_type.Command.handle")
    @patch("nps_app.management.commands.load_company.Command.handle")
    @patch("nps_app.management.commands.load_roles.Command.handle")
    @patch("nps_app.management.commands.load_user.Command.handle")
    @patch("nps_app.management.commands.load_nps.Command.handle")
    def test_load_all_data_command(
        self,
        mock_load_nps,
        mock_load_user,
        mock_load_roles,
        mock_load_company,
        mock_load_company_type,
        mock_load_country,
    ):
        call_command("load_all_data")

        # Verifica que cada comando de carga de datos se llamó
        mock_load_country.assert_called_once()
        mock_load_company_type.assert_called_once()
        mock_load_company.assert_called_once()
        mock_load_roles.assert_called_once()
        mock_load_user.assert_called_once()
        mock_load_nps.assert_called_once()
