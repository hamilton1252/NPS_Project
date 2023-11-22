from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from nps_app.domain.nps_rating_model import NPSRating
from nps_app.serializers import LowRatingSerializer


class LowRatingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        low_ratings = NPSRating.objects.filter(score__lt=4)
        serializer = LowRatingSerializer(low_ratings, many=True)
        return Response(serializer.data)
