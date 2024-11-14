from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='notificaciones', on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)