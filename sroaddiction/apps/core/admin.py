#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from .models import *

admin.site.unregister(Group)
# admin.site.unregister(Site)

class ImageInline(admin.TabularInline):
	model = Image
	extra = 1
	max_num = 10
	can_delete = True

	verbose_name = _('Image')
	verbose_name_plural = _('Images')

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1
	max_num = 10
	can_delete = True

	verbose_name = _('Video')
	verbose_name_plural = _('Videos')

class NewsInline(admin.TabularInline):
	model = News
	extra = 1
	max_num = 10
	can_delete = True

	verbose_name = _('News')
	verbose_name_plural = _('News')

class ServerAdmin(admin.ModelAdmin):
	inlines = (
		ImageInline,
		VideoInline,
		NewsInline,
	)
	fields = (
		'name', 'description', 
		('originality', 'nationality',),
		('cap', 'degree', 'mastery', 'exp_rate', 'exp_party_rate', 'gold_drop_rate', 'item_drop_rate', 'alchemy_rate',),
		('website_link', 'website_register_link',),
	)
	list_display = ('name', 'cap', 'originality', 'nationality',)
	list_filter = ('originality', 'nationality__name')
	search_fields = ('name', 'cap', 'originality', 'nationality__name',)
	ordering = ('name', 'cap', 'originality', 'nationality',)

	verbose_name = _('Server')
	verbose_name_plural = _('Servers')

admin.site.register(Server, ServerAdmin)