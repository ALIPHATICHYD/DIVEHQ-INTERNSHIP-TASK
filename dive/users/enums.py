from django.db.models import TextChoices


class Role(TextChoices):
    MANAGER = 'manager'
    ADMIN = 'admin'