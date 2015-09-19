# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.gzip import gzip_page
from django.template import RequestContext
import re
import sys
import markdown
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import UserAdmin
import datetime
import pytz
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.


@gzip_page 
def host(request):
    articles_lately = Blog.objects().order_by('-create_date')[:4]
    articles_recommend = Blog.objects().order_by('-read_numbers')[:4]
    return render_to_response('host.html',
                              {'articles_lately': articles_lately,
                               'articles_recommend': articles_recommend})


@gzip_page 
def find_all(request):
    return render_to_response('list.html', {'items': []})


@gzip_page 
def blog_list(request):
    page_num = request.GET.get('page')
    type_name = request.GET.get('type_name')
    blog_type = ArticleType.objects(type_name=type_name)
    if blog_type.count() > 0:
        blogs = Blog.objects(article_type=blog_type[0]).order_by('-create_date')
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
        article = Blog.objects(id=article_id).first()
        if not article:
            return HttpResponseRedirect('/')
        article.read_numbers += 1
        article.save()
        content = dict()
        content['article'] = article
        if request.user.is_authenticated():
            content['is_authenticated'] = True

        return render_to_response('blog_text.html',
                                  content,
                                  context_instance=RequestContext(request))


@gzip_page
@login_required(login_url="/login/")
def edit_article(request):
    if request.method == 'GET':
        article_types = ArticleType.objects()
        article_id = request.GET.get('article_id')
        article = None
        new_form = ArticleForm()
        if article_id:
            article = Blog.objects(id=article_id).first()
        return render_to_response('ArticleEdit.html',
                                  {'article_types': article_types,
                                   'article': article,
                                   'form': new_form},
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        article_title = request.POST.get('title')
        type_id = request.POST.get('article_type')
        introduction = request.POST.get('introduction')
        text = request.POST.get('content')
        keywords = request.POST.get('keywords')
        article_id = request.POST.get('article_id')
        article_type = ArticleType.objects(id=type_id).first()
        if article_title and type_id and introduction and text and keywords:
            pass
        else:
            raise Http404
        if article_id:
            article = Blog.objects(id=article_id).first()
            article.title = article_title
            article.keywords = keywords
            article.text = text
            article.article_type = article_type
            article.introduction = introduction
            article.save()
        else:
            article = Blog()
            article.title = article_title
            article.keywords = keywords
            article.text = text
            article.article_type = article_type
            article.introduction = introduction
            article.create_date = datetime.datetime.now()
            article.save()
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def delete_article(request):
    if request.method == 'GET':
        article_id = request.GET.get('id')
        article = Blog.objects(id=article_id).first()
        article.delete()


def add_new_comment(request):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip_address = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip_address = request.META['REMOTE_ADDR']
        if form.is_valid():
            pass
        else:
            return HttpResponse('表单错误')
        form = form.cleaned_data
        if not form['author_if'] == "w308346420" and form['name'] == "</Shadow>":
            raise Http404
        if not form['e_mail']:
            form['e_mail'] = None
        print form
        articles = Blog.objects(id=form['article_id'])
        if articles.count() == 0:
            raise Http404
        article = articles.first()
        req = article.add_new_comment(name=form['name'],
                                      e_mail=form['e_mail'],
                                      content=form['content'],
                                      ip_address=ip_address)
        print article.title + u"的新评论的ID为" + str(req)
        return HttpResponseRedirect('/blog?article_id=' + str(article.id))


def add_new_reply(request):
    if request.method == 'POST':
        form = AddReplyForm(request.POST)
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip_address = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip_address = request.META['REMOTE_ADDR']
        if form.is_valid():
            pass
        else:
            return HttpResponse('表单错误')
        form = form.cleaned_data
        if not form['author_if'] == "w308346420" and form['name'] == "</Shadow>":
            raise Http404
        if not form['e_mail']:
            form['e_mail'] = None
        if not form['to_reply_name']:
            form['to_reply_name'] = None
        print form
        articles = Blog.objects(id=form['article_id'])
        if articles.count() == 0:
            raise Http404
        article = articles.first()
        create_datetime = datetime.datetime.utcnow()
        print create_datetime
        req = article.add_new_reply(name=form['name'],
                                    e_mail=form['e_mail'],
                                    content=form['content'],
                                    ip_address=ip_address,
                                    to_comment_id=form['comment_id'],
                                    to_reply_name=form['to_reply_name'],
                                    create_datetime=create_datetime)
        if not req:
            raise Http404
        return HttpResponseRedirect('/blog?article_id=' + str(article.id))


@login_required(login_url='/login/')
def delete_comment(request):
    if request.method == 'POST':
        form = DeleteCommentForm(request.POST)
        if form.is_valid():
            pass
        else:
            return HttpResponse('表单出错')
        form = form.cleaned_data
        articles = Blog.objects(id=form['article_id'])
        if articles.count() == 0:
            raise Http404
        article = articles.first()
        for comment in article.comments:
            if comment.comment_id == int(form['comment_id']):
                article.comments.remove(comment)
                article.save()
                return HttpResponse('T')

        return HttpResponse('F')


@login_required(login_url='/login/')
def delete_reply(request):
    if request.method == 'POST':
        form = DeleteReplyForm(request.POST)
        if form.is_valid():
            pass
        else:
            return HttpResponse('表单出错')
        form = form.cleaned_data
        articles = Blog.objects(id=form['article_id'])
        if articles.count() == 0:
            raise Http404
        article = articles.first()
        for comment in article.comments:
            if comment.comment_id == int(form['comment_id']):
                for reply in comment.replies:
                    if reply.reply_id == int(form['reply_id']):
                        comment.replies.remove(reply)
                        article.save()
                        return HttpResponse('T')

                return HttpResponse('F')

        return HttpResponse('F')


@login_required(login_url='/login/')
def delete_article(request):
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST)
        if form.is_valid():
            pass
        else:
            return HttpResponse('表单出错')
        form = form.cleaned_data
        articles = Blog.objects(id=form['article_id'])
        if articles.count() == 0:
            raise Http404
        articles.first().delete()
        return HttpResponse('T')


# def add_article_type(request):
#     if request.method == 'GET':
#         article_types = ['python', 'js', 'linux', 'html_css', 'mac_os', 'life']
#         for article_type in article_types:
#             new_article = ArticleType(type_name=article_type)
#             new_article.save()
#         return HttpResponse('OK')


def blog_text_edit(request):
    return render_to_response('blog_text_edit.html')
