from django.core.management.base import BaseCommand
from nps_app.models import NPSRating, User
import random


class Command(BaseCommand):
    help = "Carga datos de encuestas NPS con usuarios anónimos"

    def handle(self, *args, **kwargs):
        for _ in range(500):
            user = random.choice(User.objects.all())
            nps_rating = NPSRating(
                user=user,  # Sin asociar a una persona específica
                score=random.randint(0, 10),  # Puntuación aleatoria entre 0 y 10
            )
            nps_rating.save()

        self.stdout.write(
            self.style.SUCCESS(
                "200 registros de NPS cargados exitosamente con usuarios."
            )
        )
