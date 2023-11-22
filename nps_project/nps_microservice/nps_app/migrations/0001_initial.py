# Generated by Django 4.2.7 on 2023-11-22 04:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import nps_app.domain.user_model
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_in",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_in", null=True
                    ),
                ),
                (
                    "modified_in",
                    models.DateTimeField(
                        auto_now=True, db_column="modified_in", null=True
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(db_column="email", max_length=254, unique=True),
                ),
                ("password", models.CharField(max_length=128)),
                ("username", models.CharField(max_length=128)),
            ],
            options={"db_table": "user", "ordering": ["id"],},
            managers=[("objects", nps_app.domain.user_model.UserManager()),],
        ),
        migrations.CreateModel(
            name="CompanyType",
            fields=[
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_in",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_in", null=True
                    ),
                ),
                (
                    "modified_in",
                    models.DateTimeField(
                        auto_now=True, db_column="modified_in", null=True
                    ),
                ),
                ("description", models.CharField(max_length=50)),
            ],
            options={"db_table": "company_type", "ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_in",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_in", null=True
                    ),
                ),
                (
                    "modified_in",
                    models.DateTimeField(
                        auto_now=True, db_column="modified_in", null=True
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("region", models.CharField(max_length=50)),
            ],
            options={"db_table": "country", "ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_in",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_in", null=True
                    ),
                ),
                (
                    "modified_in",
                    models.DateTimeField(
                        auto_now=True, db_column="modified_in", null=True
                    ),
                ),
                ("description", models.CharField(max_length=50)),
            ],
            options={"db_table": "role", "ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="NPSRating",
            fields=[
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_in",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_in", null=True
                    ),
                ),
                (
                    "modified_in",
                    models.DateTimeField(
                        auto_now=True, db_column="modified_in", null=True
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, db_column="date")),
                (
                    "score",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        db_column="user_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "NPS_rating", "ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_in",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_in", null=True
                    ),
                ),
                (
                    "modified_in",
                    models.DateTimeField(
                        auto_now=True, db_column="modified_in", null=True
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "country",
                    models.ForeignKey(
                        db_column="country",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nps_app.country",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        db_column="type",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nps_app.companytype",
                    ),
                ),
            ],
            options={"db_table": "company", "ordering": ["id"],},
        ),
        migrations.AddField(
            model_name="user",
            name="company",
            field=models.ForeignKey(
                db_column="company",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="nps_app.company",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ForeignKey(
                db_column="role",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="nps_app.role",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
