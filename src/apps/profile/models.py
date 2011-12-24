from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    record = models.BooleanField('Historico')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
