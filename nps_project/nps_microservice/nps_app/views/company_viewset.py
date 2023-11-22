from rest_framework import viewsets
from nps_app.domain import Company
from nps_app.serializers.company_serializer import CompanySerializer
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
