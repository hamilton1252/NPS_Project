from rest_framework import serializers
from nps_app.domain import Company


class CompanySerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ["name", "country", "type"]

    def get_country(self, obj):
        return obj.country.name if obj.country else None

    def get_type(self, obj):
        return obj.type.description if obj.type else None
