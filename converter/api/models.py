from django.db import models


class Currency(models.Model):

    name_from = models.CharField(max_length=3)
    name_to = models.CharField(max_length=3)
    amount = models.FloatField(max_length=7)
    value = models.FloatField(max_length=7)
