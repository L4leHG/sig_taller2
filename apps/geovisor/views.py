from rest_framework import response, generics, serializers

#MODELS
from .models import Marcadores

#SERIALIZER
from .serializers.serializer_geo import MarcadoresSerializerGis

class CreateMarcadorCreateListApiView(generics.ListCreateAPIView):
    serializer_class = MarcadoresSerializerGis
    queryset = Marcadores.objects.all()

    def list(self,request):
        marcadores = Marcadores.objects.all()
        serializer = MarcadoresSerializerGis(marcadores, many=True)
        return response.Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        dict_marcador = {
            'nombre' : data.get('nombre'),
            'direccion' : data.get('direccion'),
            'total_estudiantes' : data.get('total_estudiantes'),
            'geom': f"POINT ({data.get('lng') } {data.get('lat')})",
        }
        Marcadores.objects.create(**dict_marcador)
        return response.Response(1)

class UpdateMarcadorCreateListApiView(generics.UpdateAPIView):
    serializer_class = MarcadoresSerializerGis
    queryset = Marcadores.objects.all()
    
    def patch(self, request):
        data = request.data
        id_marcador = data.get('id_marcador')
        instance_marcador = Marcadores.objects.filter(id = id_marcador).first()
        instance_marcador.nombre = data.get('nombre')
        instance_marcador.direccion = data.get('direccion')
        instance_marcador.total_estudiantes = data.get('total_estudiantes')
        instance_marcador.save()
        return response.Response(1)

class DeleteMarcadorCreateListApiView(generics.DestroyAPIView):
    serializer_class = MarcadoresSerializerGis
    queryset = Marcadores.objects.all()
    
    def delete(self, request, id):
        Marcadores.objects.filter(id = id).first().delete()
        return response.Response('Marcador eliminado correctamente')

