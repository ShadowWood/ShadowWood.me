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
    read_numbers = models.IntegerField(max_length=10, default=0)

    def __unicode__(self):
        return self.title


class BlogText(models.Model):
    article = models.OneToOneField(BlogList, related_name='blog_text')
    article_body = models.TextField()

    def __unicode__(self):
        return self.article.title
