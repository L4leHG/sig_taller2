

# DJANGO
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# utilities
from apps.utils.models import BaseModel

# Utilities
class User(BaseModel, AbstractUser):
    
    email = models.EmailField(
        'direccion electronica',
        unique = True,
        error_messages= {
            'Unique':'El usuario con este email ya existe'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='El numero telefonico debe tener el formato: +999999999. Hasta 15 digitos permitido'
    )
    phone_number = models.CharField(max_length=17, blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",'first_name','last_name']

    is_client = models.BooleanField(
        'Status del usuario',
        default=True,
        help_text=(
            'Ayuda a identificar usuarios y realizar queries. '
        )
    )

    is_verified = models.BooleanField(
        'verificado',
        default=True,
        help_text = 'Configurado a verdadero cuando el usuario ha verificado su direccion de correo electronico'
    )

    def __str__(self):
        """Regreasa el nombre de usuario"""
        return self.username
    
    def get_short_name(self):
        return self.username
