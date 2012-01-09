# -*- coding: utf-8 -*-
from django.db import models
from ubigeo.models import Ubigeo

class Base(models.Model):
    ubigeo         = models.ForeignKey(Ubigeo)
    name           = models.CharField('Base', max_length = 140)
    address        = models.TextField('Dirección', blank = True, null = True)
    foundation     = models.DateField('Fundado')
    observation    = models.TextField('Observación', blank = True, null = True)
    active         = models.BooleanField('Activo', blank = True, default = True)
    #contact_number = models.CharField('Teléfono del contacto', max_length = 10)

    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'
        unique_together = ('ubigeo', 'name',)

    def __unicode__(self):
        return u'%s' % self.name
