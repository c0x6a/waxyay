# -*- coding: utf-8 -*-
from django.db import models

class Education(models.Model):
    education = models.CharField('Grado de Instrucción', max_length = 140)

    class Meta:
        verbose_name = 'Grado de Instrucción'
        verbose_name_plural = 'Grado de Instrucción'

    def __unicode__(self):
        return u'%s' % self.education

class Citizen(models.Model):
    number_document    = models.CharField('Número de Documento',max_length=8,primary_key=True)
    check_code         = models.CharField('Codigo de verificación',max_length=1, blank = True, null = True)
    number_book        = models.CharField('Número de libro',max_length=6, blank = True, null = True)
    region_code        = models.CharField('Código de Región',max_length=2, blank = True, null = True)
    province_code      = models.CharField('Código de Provincia',max_length=2, blank = True, null = True)
    district_code      = models.CharField('Código de Distrito',max_length=2, blank = True, null = True)
    paternal_surname   = models.CharField('Apellido paterno',max_length=40, blank = True, null = True)
    mother_surname     = models.CharField('Apellido materno',max_length=406, blank = True, null = True)
    name               = models.CharField('Nombres',max_length=35, blank = True, null = True)
    birth_date         = models.DateField('Fecha de Nacimiento')
    sex                = models.CharField('Sexo',max_length=1)
    degree_instruction = models.ForeignKey(Education, verbose_name='Educación')
    restriction        = models.CharField('Restricción',max_length=1, blank = True, null = True)
    document_kind      = models.CharField('Tipo de Documento',max_length=1, blank = True, null = True)
    disability         = models.IntegerField('Discapacidad', blank=True, null=True)
    
    def __unicode__(self):
        return self.number_document

    class Meta:        
        verbose_name = "Ciudadano" 
        verbose_name_plural = "Ciudadanos"
