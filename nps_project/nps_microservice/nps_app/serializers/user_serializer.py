from rest_framework import serializers
from nps_app.domain import User


class UserSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["name", "email", "company", "role"]

    def get_company(self, obj):
        """
        Método para obtener solo el nombre de la compañía.
        """
        return obj.company.name if obj.company else None

    def get_role(self, obj):
        """
        Método para obtener solo el nombre de la compañía.
        """
        return obj.role.description if obj.role else None
