from django.db import models
from django.contrib.auth.models import User
from afiliado.models import Affiliate

class Profile(User):
    affiliate = models.ForeignKey(Affiliate)
    record    = models.BooleanField('Historico')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
