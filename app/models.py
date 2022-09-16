from django.db import models


class TestIP(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(unique=True, default=1)
