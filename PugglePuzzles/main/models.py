from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Puzzle(models.Model):
    start = models.JSONField
    solution = models.JSONField
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class IPAddressUser(models.Model):
    ip_address = models.CharField(max_length=15)
