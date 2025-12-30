from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Application configuration for the Blog app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
