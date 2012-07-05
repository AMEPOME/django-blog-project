from django.contrib import admin
from django.db import models
class Post(models.Model):
  title=models.CharField(max_length=100)
  body=models.TextField()
  created=models.DateField()
  updated=models.DateField()
  def __unicode__(self):
    return self.title
class Comment(models.Model):
  body=models.TextField()
  author=models.CharField(max_length=60)
  created=models.DateField()
  updated=models.DateField()
  post=models.ForeignKey(Post)
  def __unicode__(self):
    return self.author
admin.site.register(Post)
admin.site.register(Comment)


# Create your models here.
