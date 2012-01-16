# -*- coding: utf-8 -*-
from django.db import models
from compatriota.models import Affiliate

CATEGORIA = (
            (0,'Historial nacionalista'),
            (1,'Historial político'),
            (2,'Estudios realizados'),
            (3,'Capacitaciones realizadas'),
            (4,'Porfesión'),
            (5,'Ocupación'),
            (6,'Experiencia laboral - sector privado'),
            (7,'Experiencia laboral - sector estatal'),
            )

class Record(models.Model):
    affiliate   = models.ForeignKey(Affiliate)
    #category    = models.ForeignKey('self', related_name='+', null = True, blank = True)
    category    = models.IntegerField(choices = CATEGORIA, null = True, blank = True, default = 0)
    #title       = models.CharField('Título', max_length=130)
    description = models.TextField('Descripción')
    initiation  = models.DateField('Inicio')
    end         = models.DateField('Fin', null = True, blank = True)

    def __unicode__(self):
        return self.title

    class Meta:        
        verbose_name = "Historial" 
        verbose_name_plural = "Historiales"
