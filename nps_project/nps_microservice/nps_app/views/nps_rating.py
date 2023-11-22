from rest_framework.views import APIView
from rest_framework.response import Response
from nps_app.models import NPSRating
from nps_app.serializers import NPSRatingSerializer
from nps_app.decorators import log_event


class NPSRatingView(APIView):
    @log_event
    def post(self, request):
        serializer = NPSRatingSerializer(data=request.data)
        if serializer.is_valid():
            nps_rating = serializer.save(
                user=request.user if request.user.is_authenticated else None
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
