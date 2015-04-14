# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.views.generic.base import RedirectView
from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^abc_shadow_159357/', include(admin.site.urls)),
    url(r'^$', host),
    url(r'^blog_list$', blog_list),
    url(r'^blogs$', blogs_get),
    url(r'^about_me$', about_me),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_DIR}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMG_DIR}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_DIR}),
    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.FONTS_DIR}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR}),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/img/1.ico')),
    url(r'^comments/', include('django_comments.urls')),
)

# from django.conf import settings
# if settings.DEBUG is False:
#     urlpatterns += patterns('',
#                             url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
#                                 {'document_root': settings.CSS_DIR}),
#                             url(r'^img/(?P<path>.*)$', 'django.views.static.serve',
#                                 {'document_root': settings.IMG_DIR}),
#                             )
