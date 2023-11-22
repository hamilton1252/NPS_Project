import json
import random
from django.core.management.base import BaseCommand
from nps_app.models import User, Company, Role


class Command(BaseCommand):
    help = "Carga datos de usuarios desde un archivo JSON y asigna company y role aleatoriamente"

    def handle(self, *args, **kwargs):
        # Asegurarse de que existen datos para Company y Role
        if not Company.objects.exists() or not Role.objects.exists():
            self.stdout.write(
                self.style.ERROR("Asegúrese de tener datos para Company y Role")
            )
            return

        # Leer el archivo JSON
        with open("users.json", "r", encoding="utf-8") as file:
            users_data = json.load(file)

            for user_data in users_data:
                # Asignar company y role aleatoriamente
                user_data["company"] = random.choice(Company.objects.all())
                user_data["role"] = random.choice(Role.objects.all())

                # Crear usuario
                User.objects.create_user(
                    email=user_data["email"],
                    name=user_data["name"],
                    password=user_data["password"],
                    username=user_data["username"],
                    company=user_data["company"],
                    role=user_data["role"],
                )

        self.stdout.write(self.style.SUCCESS("Usuarios cargados exitosamente."))
