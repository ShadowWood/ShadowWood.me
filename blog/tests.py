# -*- coding: utf-8 -*-
from django.test import TestCase
from models import *
# Create your tests here.


def create_comments():
    article = Blog.objects().order_by('-id').first()
    print article.add_new_comment(name="测试1",
                                  e_mail="1234567789@qq.com",
                                  content="测试评论",
                                  ip_address="192.168.1.1")


def delete_all_comments():
    replies = Reply.objects()
    for reply in replies:
        reply.delete()
    print replies.count()
    comments = Comment.objects()
    for comment in comments:
        comment.delete()
    print comments.count()

    article = Blog.objects().first()
    article.comments = None
    article.save()


def create_reply():
    article = Blog.objects().order_by('-id').first()
    print article.add_new_reply(name=u"回复1",
                                content=u"<h3>回复楼上safd1111</h3>",
                                ip_address="192.168.1.3",
                                e_mail="123@qq.com",
                                to_comment_id=1,
                                to_reply_id=1)