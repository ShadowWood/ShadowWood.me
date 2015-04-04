from django.db import models

# Create your models here.


class BlogType(models.Model):
    type_id = models.IntegerField(max_length=2)
    type_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.type_name


class BlogList(models.Model):
    date = models.DateTimeField(max_length=10)
    title = models.CharField(max_length=20)
    type = models.ForeignKey(BlogType)
    keywords = models.CharField(max_length=20, null=True, blank=True)
    introduction = models.TextField()

    def __unicode__(self):
        return self.title


class BlogText(models.Model):
    article = models.OneToOneField(BlogList)
    article_body = models.TextField()

    def __unicode__(self):
        return self.article.title


class Discuss(models.Model):
    belong = models.ForeignKey(BlogList, related_name="content")
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Answer(models.Model):
    discuss = models.ForeignKey(Discuss)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.discuss.name
