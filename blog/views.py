# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.http import HttpResponseRedirect, HttpResponse, Http404
import re
import sys
import markdown
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.


def host(request):
    return render_to_response('host.html')


def find_all(request):
    blogs = BlogList.objects.all()
    return render_to_response('list.html', {'items': blogs})


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


def about_me(request):
    return render_to_response('about_me.html')


def blogs_get(request):
    if request.method == 'GET':
        article_id = request.GET.get('article_id')
        article = BlogList.objects.filter(id=article_id)
        if article.count() == 0:
            return HttpResponseRedirect('/')
        blog_mes = BlogText.objects.filter(article=article[0])
        blog_article = markdown.markdown(blog_mes[0].article_body)
        return render_to_response('blog_text.html',
                                  {'item': blog_article,
                                   'article': article[0]})