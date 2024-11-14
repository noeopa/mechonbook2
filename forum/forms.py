from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Usuario
class RegistroForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label='Fecha de nacimiento'
    )
    foto = forms.ImageField(required=False, label='Foto de perfil')
   
    

    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'fecha_nacimiento']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@usm.cl'):
            raise forms.ValidationError("El correo debe ser @usm.cl")
        return email

class EditarPerfilForm(UserChangeForm):
    password = None  # Excluir el campo de contraseña del formulario de edición general

    class Meta:
        model = Usuario  # Usar el modelo de usuario personalizado
        fields = ['username', 'foto']  # Campos que el usuario puede editar

# Formulario para cambiar la contraseña
class CambiarContraseñaForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']
