from django.db import models
from django.db import models

class IPAddressUser(models.Model):
    ip_address = models.CharField(max_length=15)
