from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_SUPERADMIN = 'superadmin'
    ROLE_RESTAURANT_ADMIN = 'restaurant_admin'

    ROLE_CHOICES = [
        (ROLE_SUPERADMIN, 'Super Admin'),
        (ROLE_RESTAURANT_ADMIN, 'Restaurant Admin'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_RESTAURANT_ADMIN
    )
    phone = models.CharField(max_length=20, blank=True)

    def is_superadmin(self):
        return self.role == self.ROLE_SUPERADMIN

    def is_restaurant_admin(self):
        return self.role == self.ROLE_RESTAURANT_ADMIN

    def __str__(self):
        return f"{self.email} [{self.get_role_display()}]"
