from django.db import models


class Input(models.Model):
    input_data = models.JSONField(primary_key=True)

# Create your models here.
