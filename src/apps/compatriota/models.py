# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from ubigeo.models import Ubigeo
from base.models import Base
from ciudadano.models import Citizen
from carrera.models import Education,Occupation,Profession

TIPO = (
    (1, u'Público'),
    (2, u'Interno'),
)

ESTADO = (
    (1, u'Activo'),
    (2, u'Expulsado'),
    (2, u'Renunció'),
)

class Affiliate(models.Model):
    citizen         = models.OneToOneField(Citizen)
    education       = models.ForeignKey(Education, blank = True, null = True)
    occupation      = models.ForeignKey(Occupation, blank = True, null = True)
    profession      = models.ForeignKey(Profession, blank = True, null = True)
    base            = models.ForeignKey(Base)
    ubigeo_now      = models.ForeignKey(Ubigeo, blank = True, null = True)
    #ubigeo_birth    = models.ForeignKey(Ubigeo, blank = True, null = True)
    #date_birth      = models.DateField('Fecha de nacimiento', blank = True, null = True)
    address         = models.TextField('Dirección', blank = True, null = True)
    address_home    = models.TextField('Dirección actual', blank = True, null = True)
    phone           = models.CharField('Teléfono', max_length = 8, blank = True, null = True)
    cellphone       = models.CharField('Celular', max_length = 12, blank = True, null = True)
    email           = models.EmailField('E-Mail', blank = True, null = True)
    another_contact = models.TextField('Otro medio de contacto', blank = True, null = True)
    another_study   = models.TextField('Capacitación', blank = True, null = True)
    affidavit       = models.BooleanField('Declaración Jurada', default = True)
    foto            = models.ImageField('Foto', upload_to = 'Foto/', blank = True, null = True)
    kind            = models.IntegerField('Tipo', choices=TIPO, blank = True, null = True)
    state           = models.IntegerField('Estado', choices=ESTADO, blank = True, null = True)
    date_record     = models.DateField('Fecha de registro', auto_now_add=True, editable = False, default = datetime.today())
    date_enrollment = models.DateField('Fecha de afiliación')

    class Meta:
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'

    def __unicode__(self):
        return u'%s $s; %s' % (self.paternal_surname, self.mother_surname, self.name)
     
