from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .user_model import User
from nps_app.core_base.base_model import BaseModel


class NPSRating(BaseModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="user_id", null=True, blank=True
    )
    date = models.DateTimeField(auto_now_add=True, db_column="date")
    score = score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    class Meta:
        db_table = "NPS_rating"
        ordering = ["id"]
