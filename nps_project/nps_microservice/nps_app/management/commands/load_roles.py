import json
from django.core.management.base import BaseCommand
from nps_app.domain import Role


class Command(BaseCommand):
    help = "Carga datos de países y tipos de personas desde archivos JSON"

    def handle(self, *args, **kwargs):
        # Cargar tipos de personas
        with open("roles.json", "r", encoding="utf-8") as file:
            person_types_data = json.load(file)
            for person_type_data in person_types_data:
                Role.objects.get_or_create(**person_type_data)

        self.stdout.write(self.style.SUCCESS("Datos de Roles cargados exitosamente."))
