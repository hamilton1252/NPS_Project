from rest_framework import viewsets
from nps_app.domain import Role
from nps_app.serializers.role_serializer import RoleSerializer
from rest_framework.permissions import IsAuthenticated


class RoleViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
