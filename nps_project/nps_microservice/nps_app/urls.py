from nps_app.views import CompanyViewSet, RoleViewset, LowRatingView, NPSRatingView
from rest_framework.routers import SimpleRouter
from nps_app.views.reports import (
    TopDetractorCountriesView,
    TopPromoterPersonTypesView,
    MonthlyRatingsView,
)
from django.urls import path


router = SimpleRouter()
router.register(r"company", CompanyViewSet, basename="companies")
router.register(r"rol", RoleViewset, basename="roles")

urlpatterns = router.urls + [
    path("low_rating/", LowRatingView.as_view(), name="obtain_low_rating"),
    path("nps_rating/", NPSRatingView.as_view(), name="nps_rating"),
    path(
        "report_detractor/",
        TopDetractorCountriesView.as_view(),
        name="report_detractor",
    ),
    path(
        "report_promoter/",
        TopPromoterPersonTypesView.as_view(),
        name="report_promoter",
    ),
    path(
        "report_monthly/",
        MonthlyRatingsView.as_view(),
        name="report_monthly",
    ),
]
