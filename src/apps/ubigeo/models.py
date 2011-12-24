# -*- coding: utf-8 -*-
from django.db import models

class Ubigeo(models.Model):
    ubigeo = models.CharField('Ubigeo', max_length=8)
    name   = models.CharField('Nombre', max_length=140)
    parent = models.ForeignKey('self', related_name='+', null = True, blank = True)

    class Meta:
        verbose_name = 'Ubigeo'
        verbose_name_plural = 'Ubigeos'

    def __unicode__(self):
        return u'%s' % self.name
