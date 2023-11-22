# from .views import UserViewset
from .views import MyTokenObtainPairView
from rest_framework.routers import SimpleRouter
from django.urls import path


router = SimpleRouter()

urlpatterns = router.urls + [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
