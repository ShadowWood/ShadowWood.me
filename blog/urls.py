from django.conf.urls import patterns, include, url
from django.contrib import admin
import Myblog.settings
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog_list$', blog_list),
    url(r'^blog$', blogs_get),
    url(r'^about_me$', about_me),
    url(r'^$', host),
    url(r'^edit_blog$', edit_article),
    url(r'^add_new_comment$', add_new_comment),
    url(r'^add_new_reply$', add_new_reply),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    # option
    url(r'^delete_comment$', delete_comment),
    url(r'^delete_reply$', delete_reply),
    url(r'^delete_article$', delete_article),
    # url(r'^add_article_type$', add_article_type)
    url(r'^test$', 'django.contrib.auth.views.login', {'template_name': 'test.html'}),
    url(r'^blog_text_edit$', blog_text_edit)

)