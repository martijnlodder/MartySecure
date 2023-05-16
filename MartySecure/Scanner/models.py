from django.db import models


class Vulnerability(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    services = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    severity = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ValidatedResult(models.Model):
    port = models.IntegerField()
    service = models.CharField(max_length=50)
    version = models.CharField(max_length=50, blank=True)
    vulnerability = models.CharField(max_length=50)
    description = models.TextField()
    severity = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.service} on port {self.port} ({self.vulnerability})'
