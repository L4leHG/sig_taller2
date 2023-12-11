from django.urls import path
from .views import (
    CreateMarcadorCreateListApiView, UpdateMarcadorCreateListApiView, DeleteMarcadorCreateListApiView
    )

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('create/marcadores',CreateMarcadorCreateListApiView.as_view(), name='create_marcadores'),
    path('update/marcadores',UpdateMarcadorCreateListApiView.as_view(), name='update_marcadores'),
    path('delete/marcadores/<id>',DeleteMarcadorCreateListApiView.as_view(), name='delete_marcadores'),
]