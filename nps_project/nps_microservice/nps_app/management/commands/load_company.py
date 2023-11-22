import json
import random
from django.core.management.base import BaseCommand
from nps_app.models import Company, Country, CompanyType


class Command(BaseCommand):
    help = "Carga datos de compañías desde un archivo JSON y asigna country y type aleatoriamente"

    def handle(self, *args, **kwargs):
        with open("companies.json", "r", encoding="utf-8") as file:
            companies_data = json.load(file)

            # Asegurarse de que existen países y tipos de compañía
            if not Country.objects.exists() or not CompanyType.objects.exists():
                self.stdout.write(
                    self.style.ERROR(
                        "Asegúrese de tener países y tipos de compañía en la base de datos."
                    )
                )
                return

            for company_data in companies_data:
                country = random.choice(Country.objects.all())
                company_type = random.choice(CompanyType.objects.all())

                Company.objects.create(
                    name=company_data["name"], country=country, type=company_type
                )

        self.stdout.write(
            self.style.SUCCESS("Datos de compañías cargados exitosamente.")
        )
