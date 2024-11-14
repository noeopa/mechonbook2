
from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EditarPerfilForm, CambiarContraseñaForm
from .models import Usuario, Notificacion
from django.db import models


# Vista para manejar el registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES) # Formulario que incluye campos y archivos
        if form.is_valid():                              # Valida los datos del formulario
            form.save()                                   # Guarda el usuario 
            messages.success(request, 'Registro Exitoso')                                 
            return redirect('login')                     # Redirige a la página de inicio
        else:
            messages.error(request, 'Registro Inválido')
    else:
        form = RegistroForm()                            # Si la solicitud es GET, mostrar el formulario vacio
        
    return render(request, 'forum/registro.html', {'form': form})




def pantalla_bienvenida(request):
    # Redirigir al home si el usuario está autenticado
    if request.user.is_authenticated:
        return redirect('home')

    # Mostrar la pantalla de bienvenida para usuarios no autenticados
    return render(request, 'forum/bienvenida.html')

# Vista para manejar la página principal
@login_required
def home(request):
    return render(request, 'forum/home.html')         # Renderiza la plantilla de la pagina principal

def perfil(request):
    return render(request, 'forum/perfil.html')


# Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actualización Exitosa')
            return redirect('editar_perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'forum/editar_perfil.html', {'form': form})

# Vista para cambiar la contraseña del usuario
@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = CambiarContraseñaForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Mantener la sesión iniciada después del cambio
            messages.success(request, 'Contraseña Modificada Exitosamente')
            return redirect('editar_perfil')
    else:
        form = CambiarContraseñaForm(user=request.user)
    return render(request, 'forum/cambiar_contraseña.html', {'form': form})


   
  
