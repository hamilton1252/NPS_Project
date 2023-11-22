import uuid
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

# from safedelete.models import SOFT_DELETE
from nps_app.core_base.managers import BasicManager


class BaseModel(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_in = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_column="created_in",
    )
    modified_in = models.DateTimeField(
        auto_now=True,
        null=True,
        db_column="modified_in",
    )

    objects = BasicManager()

    class Meta:
        abstract = True
