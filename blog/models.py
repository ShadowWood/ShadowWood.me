# -*- coding: utf-8 -*-
from pymongo import *
from mongoengine import *
import datetime
from django import forms
# Create your models here.
con = connect('blog',
              tz_aware=True,
              host='localhost:27017',
              read_preference=ReadPreference.PRIMARY)


class ArticleType(Document):
    type_name = StringField()


class Reply(EmbeddedDocument):
    reply_id = IntField()
    name = StringField(max_length=20)
    create_date = DateTimeField(required=True)
    content = StringField(default=None)
    ip_address = StringField(max_length=30)
    to_reply_name = StringField(max_length=20, default=None)
    e_mail = EmailField(default=None)


class Comment(EmbeddedDocument):
    comment_id = IntField()
    name = StringField(max_length=20)
    create_date = DateTimeField(required=True)
    content = StringField(default=None)
    ip_address = StringField(max_length=30)
    replies = ListField(EmbeddedDocumentField(Reply), default=None)
    e_mail = EmailField(default=None)


class Blog(Document):
    title = StringField(required=True)
    text = StringField()
    keywords = StringField(max_length=30)
    create_date = DateTimeField()
    read_numbers = IntField(default=0)
    introduction = StringField(max_length=100)
    article_type = ReferenceField(ArticleType)
    comments = ListField(EmbeddedDocumentField(Comment), default=None)

    def add_new_comment(self, name, content, ip_address, e_mail=None):
        if self.comments:
            new_id = self.comments[-1].comment_id + 1
        else:
            new_id = 1
        new_comment = Comment(name=name,
                              content=content,
                              ip_address=ip_address,
                              e_mail=e_mail,
                              comment_id=new_id,
                              create_date=datetime.datetime.now())
        if self.comments:
            self.comments.append(new_comment)
        else:
            self.comments = [new_comment]

        self.save()
        return new_id

    def delete_comment(self, comment_id):
        if not self.comments:
            return False

        delete_comment = None
        comment_id = int(comment_id)

        for comment in self.comments:
            if comment.comment_id == comment_id:
                delete_comment = comment
        self.comments.remove(delete_comment)
        self.save()
        return True

    def add_new_reply(self, name, content, ip_address, create_datetime ,e_mail=None, to_comment_id=None, to_reply_name=None):
        to_comment = None
        if not to_comment_id:
            return False
        to_comment_id = int(to_comment_id)
        for comment in self.comments:
            if comment.comment_id == to_comment_id:
                to_comment = comment
                break

        if not to_comment:
            return False

        if to_comment.replies:
            new_id = to_comment.replies[-1].reply_id + 1
        else:
            new_id = 1

        print str(new_id) + "create"

        new_reply = Reply(name=name,
                          content=content,
                          ip_address=ip_address,
                          e_mail=e_mail,
                          reply_id=new_id,
                          to_reply_name=to_reply_name,
                          create_date=create_datetime
                          )
        if new_id == 1:
            to_comment.replies = [new_reply]
        else:
            to_comment.replies.append(new_reply)

        self.save()
        return new_id


class AddCommentForm(forms.Form):
    name = forms.CharField(max_length=20)
    e_mail = forms.EmailField(required=False)
    # author_if == "w308346420"
    author_if = forms.CharField(required=False)
    article_id = forms.CharField(max_length=100)
    content = forms.CharField()


class AddReplyForm(forms.Form):
    article_id = forms.CharField(max_length=100)
    name = forms.CharField(max_length=20)
    e_mail = forms.EmailField(required=False)
    # author_if == "w308346420"
    author_if = forms.CharField(required=False)
    comment_id = forms.CharField(max_length=100)
    content = forms.CharField()
    to_reply_name = forms.CharField(max_length=20, required=False)


class DeleteCommentForm(forms.Form):
    article_id = forms.CharField(max_length=100)
    comment_id = forms.CharField(max_length=100)


class DeleteReplyForm(forms.Form):
    article_id = forms.CharField(max_length=100)
    comment_id = forms.CharField(max_length=100)
    reply_id = forms.CharField(max_length=100)


class DeleteArticleForm(forms.Form):
    article_id = forms.CharField(max_length=100)


from DjangoUeditor.commands import UEditorEventHandler


class myEventHander(UEditorEventHandler):
    def on_selectionchange(self):
        return """
             $('#submit_article').click(function(){
                var html = id_content.getContent();
                console.log(html)
                $('#content').val(html);
                $('#article_mes').submit();
             })
	     $(document).ready(function(){
       $("#ueditor_0").contents().find("head").append("<link href='/css/flat-ui.min.css' rel='stylesheet'>");
    });	
            """


from DjangoUeditor.forms import UEditorField


class ArticleForm(forms.Form):
    content = UEditorField("",
                           initial=u"请输入文章内容",
                           width=800,
                           height=800,
                           toolbars="full",
                           imagePath="img/",
                           filePath="file/",
                           upload_settings={},
                           command=None,
                           event_handler=myEventHander())



