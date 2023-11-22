from django.db import models
from .country_model import Country
from .company_type_model import CompanyType
from nps_app.core_base.base_model import BaseModel


class Company(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column="country")
    type = models.ForeignKey(
        CompanyType, on_delete=models.CASCADE, db_column="type", null=True
    )

    class Meta:
        db_table = "company"
        ordering = ["id"]
