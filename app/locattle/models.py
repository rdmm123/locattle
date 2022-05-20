from django.db import models

# Create your models here.
class CattleLocation(models.Model):
    depto = models.IntegerField()
    farm = models.IntegerField()
    cow = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Vaca: {self.cow} | Finca: {self.farm} | Departamento: {self.depto}"

    class Meta:
        db_table = "cattle_location"