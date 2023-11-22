from django.db import models
from nps_app.core_base.base_model import BaseModel


class Role(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)

    class Meta:
        db_table = "role"
        ordering = ["id"]
