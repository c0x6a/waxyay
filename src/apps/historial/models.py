# -*- coding: utf-8 -*-
from django.db import models
from compatriota.models import Affiliate

class Record(models.Model):
    affiliate   = models.ForeignKey(Affiliate)
    category    = models.ForeignKey('self', related_name='+', null = True, blank = True)
#    title       = models.CharField('Título', max_length=130)
    description = models.TextField('Descripción')
    initiation  = models.DateField('Inicio')
    end         = models.DateField('Fin', null = True, blank = True)
#    parent      = models.ForeignKey('self', related_name='+', null = True, blank = True)

    def __unicode__(self):
        return self.title

    class Meta:        
        verbose_name = "Historial" 
        verbose_name_plural = "Historiales"

#class Category(models.Model):
#    category = models.CharField('Categoría', max_length=140)

#class Item(models.Model):
#    category    = models.ForeignKey(Category)
#    description = models.TextField('Descripción')
#    initiation  = models.DateField('Inicio')
#    end         = models.DateField('Fin', null = True, blank = True)
