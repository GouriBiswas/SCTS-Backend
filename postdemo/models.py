from django.db import models

# Create your models here.


class Coil(models.Model):
    coil_name = models.CharField(max_length=100)
    coil_type = models.CharField(max_length=100)
    weight = models.FloatField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.coil_name
