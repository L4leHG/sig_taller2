from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from ..models import Marcadores

class MarcadoresSerializerGis(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    id_marcador = serializers.SerializerMethodField()
    class Meta:
        model = Marcadores
        geo_field = "geom"
        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id_marcador', 'nombre', 'direccion', 'total_estudiantes')
    
    def get_id_marcador(self, obj):
        return obj.id