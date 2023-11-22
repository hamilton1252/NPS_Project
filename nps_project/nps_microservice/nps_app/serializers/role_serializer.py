from rest_framework import serializers
from nps_app.domain import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "description"]
