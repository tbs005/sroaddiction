#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .countries import CountryField

class Nationality(models.Model):
	'''
	'''
	name = models.CharField(_('nationality'), max_length=64, help_text=_('Nationality'))
	country = CountryField()

	class Meta:
		verbose_name = _('Nationality')
		verbose_name_plural = _('Nationalities')

	def __unicode__(self):
		return u'Nationality %s' % (self.name.lower())

class Server(models.Model):
	'''
	'''
	ORIGINAL = 'ORIGINAL'
	PRIVATE = 'PRIVATE'
	ORIGINALITY = (
		(ORIGINAL, 'Original'),
		(PRIVATE, 'Private')
	)

	name = models.CharField(_('name'), max_length=32, help_text=_('Server name'))
	description = models.TextField(_('description'), max_length=1024, blank=True, help_text=_('Description'))
	originality = models.CharField(_('originality'), max_length=8, choices=ORIGINALITY, help_text=_('Originality'))
	nationality = models.ForeignKey(Nationality, verbose_name=_('nationality'), help_text=_('Server nationality'))
	cap = models.CharField(_('cap'), max_length=8, blank=True, help_text=_('Server CAP'))
	degree = models.CharField(_('degree'), max_length=8, blank=True, help_text=_('Server degree'))
	mastery = models.CharField(_('mastery'), max_length=8, blank=True, help_text=_('Server mastery'))
	exp_rate = models.CharField(_('exp rate'), max_length=8, blank=True, help_text=_('Server EXP rate'))
	exp_party_rate = models.CharField(_('exp party rate'), max_length=8, blank=True, help_text=_('Server EXP party rate'))
	gold_drop_rate = models.CharField(_('gold drop rate'), max_length=8, blank=True, help_text=_('Server gold drop rate'))
	item_drop_rate = models.CharField(_('item drop rate'), max_length=8, blank=True, help_text=_('Server item drop rate'))
	alchemy_rate = models.CharField(_('alchemy rate'), max_length=8, blank=True, help_text=_('Server alchemy rate'))
	website_link = models.URLField(_('website link'), blank=True, help_text=_('Server website'))
	website_register_link = models.URLField(_('website register link'), blank=True, help_text=_('Server website register link'))

	class Meta:
		verbose_name = _('Server')
		verbose_name_plural = _('Servers')

	def __unicode__(self):
		return u'Server %s' % (self.name.lower())

class Image(models.Model):
	'''
	'''
	image = models.FileField(upload_to='/media/')
	server = models.ForeignKey(Server)

	class Meta:
		verbose_name = _('Image')
		verbose_name_plural = _('Images')

	def __unicode__(self):
		return u' '

class Video(models.Model):
	'''
	'''
	url = models.CharField(_('url'), max_length=64, help_text=_('Video url'))
	server = models.ForeignKey(Server)

	class Meta:
		verbose_name = _('Video')
		verbose_name_plural = _('Videos')

	def __unicode__(self):
		return u' '

class News(models.Model):
	'''
	'''
	title = models.CharField(_('title'), max_length=64, help_text=_('News title'))
	body = models.TextField(_('body'), max_length=512, help_text=_('News body'))
	server = models.ForeignKey(Server, verbose_name=_('Server'), help_text=_('Server'))
	
	class Meta:
		verbose_name = _('News')
		verbose_name_plural = _('News')

	def __unicode__(self):
		return u'New %s' % (self.name.lower())