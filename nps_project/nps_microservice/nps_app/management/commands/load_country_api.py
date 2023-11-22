import requests
from django.core.management.base import BaseCommand
from nps_app.domain import Country


class Command(BaseCommand):
    help = "Carga datos de países desde una API externa"

    def handle(self, *args, **kwargs):
        # URL de la API de países (ajustar según la API específica que estás utilizando)
        url = "https://restcountries.com/v3.1/all"

        # Haciendo la solicitud a la API
        response = requests.get(url)
        if response.status_code == 200:
            countries_data = response.json()

            # Procesar y cargar los datos
            for country_data in countries_data:
                # Asumiendo que la API proporciona un campo 'name' y 'region'
                # Ajustar según la estructura real de los datos de la API
                name = country_data.get("name", {}).get("common")
                region = country_data.get("region")
                if name and region:
                    Country.objects.get_or_create(name=name, region=region)

            self.stdout.write(
                self.style.SUCCESS(
                    "Datos de países cargados exitosamente desde la API."
                )
            )
        else:
            self.stdout.write(
                self.style.ERROR(
                    "Error al cargar datos desde la API: Estado "
                    + str(response.status_code)
                )
            )
