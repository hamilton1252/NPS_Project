from django.core.management.base import BaseCommand
from .load_country_api import Command as LoadCountriesCommand
from .load_roles import Command as LoadRolesCommand
from .load_user import Command as LoadUsersCommand
from .load_nps import Command as LoadNPSDataCommand
from .load_company_type import Command as LoadCompanyTypeCommand
from .load_company import Command as LoadCompanyCommand


class Command(BaseCommand):
    help = "Ejecuta todos los scripts de carga de datos"

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando la carga de datos...")

        # Ejecutar cada script de carga de datos
        LoadCountriesCommand().handle()
        LoadCompanyTypeCommand().handle()
        LoadCompanyCommand().handle()
        LoadRolesCommand().handle()
        LoadUsersCommand().handle()
        LoadNPSDataCommand().handle()

        self.stdout.write(
            self.style.SUCCESS("Todos los datos han sido cargados exitosamente.")
        )
