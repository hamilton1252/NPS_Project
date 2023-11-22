from rest_framework import serializers
from nps_app.models import NPSRating


class NPSRatingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = NPSRating
        fields = ["user", "score", "date"]

    def get_user(self, obj):
        return obj.user.name if obj.user else None
