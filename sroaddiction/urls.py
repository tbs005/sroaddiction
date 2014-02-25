from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sroaddiction.apps.frontend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
