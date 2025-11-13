from django.db import models

class CityRawData(models.Model):
    city = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=128)
    info = models.TextField(blank=True, null=True)
    raw = models.JSONField()  # population, founded, wikidata_raw
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
