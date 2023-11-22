from rest_framework import serializers
from nps_app.domain.nps_rating_model import NPSRating
from .user_serializer import UserSerializer


class LowRatingSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(read_only=True, source="user")

    class Meta:
        model = NPSRating
        fields = ["user_info", "score", "date"]
