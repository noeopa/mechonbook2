
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static  
from forum.views import home
from forum import views as forum_views

# Definición de las rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),                                 # Ruta para el panel de administración
    path('home/', forum_views.home, name='home'),                 # Ruta de la Página Home
    path('', forum_views.pantalla_bienvenida, name='bienvenida'), # Página inicial (bienvenida)
    path('forum/', include('forum.urls')),                     # Incluir rutas de la app usuarios                      # Incluir rutas de la app matches
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
                                      # Configuración para servir archivos multimedia en desarrollo
                                                  