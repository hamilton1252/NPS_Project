from django.db.models import Count, Q, F
from nps_app.models import NPSRating
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import TruncMonth


class TopDetractorCountriesView(APIView):
    def get(self, request):
        detractor_counts = (
            NPSRating.objects.filter(score__lte=6)
            .annotate(company=F("user__company__name"))
            .values("company")
            .annotate(detractor_count=Count("id"))
            .order_by("-detractor_count")[:3]
        )
        data = list(detractor_counts)
        return Response(data)


class TopPromoterPersonTypesView(APIView):
    def get(self, request):
        promotor_counts = (
            NPSRating.objects.filter(score__gte=9)
            .annotate(role=F("user__role__description"))
            .values("role")
            .annotate(promotor_count=Count("id"))
            .order_by("-promotor_count")
        )
        data = list(promotor_counts)
        return Response(data)


class MonthlyRatingsView(APIView):
    def get(self, request):
        monthly_ratings = (
            NPSRating.objects.annotate(
                month=TruncMonth("date"),
                country_name=F(
                    "user__company__country__name"
                ),  # Renombrar el campo aquí
            )
            .values("month", "country_name")  # Usar el nuevo nombre del campo
            .annotate(
                promotor_count=Count("id", filter=Q(score__gte=9)),
                detractor_count=Count("id", filter=Q(score__lte=6)),
            )
            .order_by("month", "country_name")
        )
        data = list(monthly_ratings)
        return Response(data)
