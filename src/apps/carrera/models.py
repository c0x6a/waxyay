# -*- coding: utf-8 -*-
from django.db import models

class Education(models.Model):
    education = models.CharField('Grado de Instrucción', max_length = 140, unique = True)

    class Meta:
        verbose_name = 'Grado de Instrucción'
        verbose_name_plural = 'Grado de Instrucción'

    def __unicode__(self):
        return u'%s' % self.education

class Occupation(models.Model):
    occupation = models.CharField('Ocupación', max_length = 140, unique = True)

    class Meta:
        verbose_name = 'Ocupación'
        verbose_name_plural = 'Ocupaciónes'

    def __unicode__(self):
        return u'%s' % self.occupation

class Profession(models.Model):
    profession = models.CharField('Profesión', max_length = 140, unique = True)

    class Meta:
        verbose_name = 'Profesión'
        verbose_name_plural = 'Profesiónes'

    def __unicode__(self):
        return u'%s' % self.profession
