# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.gzip import gzip_page
import re
import sys
import markdown
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
import datetime
import pytz
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.


@gzip_page 
def host(request):
    articles_lately = BlogList.objects.order_by('-date').all()[:4]
    articles_recommend = BlogList.objects.order_by('-read_numbers').all()[:4]
    return render_to_response('host.html',
                              {'articles_lately': articles_lately,
                               'articles_recommend': articles_recommend})


@gzip_page 
def find_all(request):
    blogs = BlogList.objects.all()
    return render_to_response('list.html', {'items': blogs})


@gzip_page 
def blog_list(request):
    page_num = request.GET.get('page')
    type_name = request.GET.get('type_name')
    blog_type = BlogType.objects.filter(type_name=type_name)
    if blog_type.count() > 0:
        blogs = BlogList.objects.order_by('-date').filter(type=blog_type[0])
        paginator = Paginator(blogs, 6)
        try:
            blogs = paginator.page(page_num)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        except:
            blogs = None
    else:
        blogs = None
    return render_to_response('list.html', {'items': blogs, 'type': type_name})


@gzip_page 
def about_me(request):
    return render_to_response('about_me.html')


@gzip_page 
def blogs_get(request):
    if request.method == 'GET':
        article_id = request.GET.get('article_id')
        article = BlogList.objects.get(id=article_id)
        if not article:
            return HttpResponseRedirect('/')
        blog_mes = BlogText.objects.filter(article=article)
        article.read_numbers += 1
        article.save()
        blog_article = markdown.markdown(blog_mes[0].article_body)
        return render_to_response('blog_text.html',
                                  {'item': blog_article,
                                   'article': article})
