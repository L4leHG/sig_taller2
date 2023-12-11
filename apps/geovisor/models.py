from django.contrib.gis.db import models

class Marcadores(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    nombre = models.TextField()
    direccion = models.TextField(null=True)
    total_estudiantes = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.PointField(srid=4326,null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return str(self.id)

