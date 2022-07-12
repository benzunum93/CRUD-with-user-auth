from django.urls import path
from . import views
from django.conf import settings #Importar archivo de conf de django
from django.contrib.staticfiles.urls import static #Para manejar archivos estaticos como imagenes

urlpatterns = [

    path('',views.inicio, name='Inicio'),
    
    path('libros',views.index_libreria, name='Libros'),
    path('libros/c',views.crear_libreria, name='Crear'),
    path('libros/e/<int:id>',views.editar_libreria, name='Editar'),
    path('d/<int:id> ',views.eliminar_libreria, name='Eliminar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)