# -*- coding: utf-8 -*-
from django.db import models
from afiliado.models import Affiliate

class Record(models.Model):
    affiliate = models.ForeignKey(Affiliate)
    title     = models.CharField('Título', max_length=130)
    duration  = models.CharField('Duración', max_length=130)
    parent    = models.ForeignKey('self', related_name='+', null = True, blank = True)

    def __unicode__(self):
        return self.title

    class Meta:        
        verbose_name = "Historial" 
        verbose_name_plural = "Historiales"
