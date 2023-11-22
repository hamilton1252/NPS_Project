from django.db import models
from .company_model import Company
from .role_model import Role
from nps_app.core_base.base_model import BaseModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Los usuarios deben tener un email.")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, name, password, **extra_fields)


class User(AbstractUser, BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False, unique=True, db_column="email", null=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, db_column="company", null=True
    )
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, db_column="role", null=True
    )
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=128, null=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        db_table = "user"
        ordering = ["id"]
