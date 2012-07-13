from django.contrib import admin
from django.db import models

class Post(models.Model):
  title=models.CharField(max_length=100)
  body=models.TextField()
  created=models.DateField()
  updated=models.DateField()

  
  def __unicode__(self):
    return self.title
  def get_absolute_url(self):
       return "/blog/posts/%i/true" % self.id

class Comment(models.Model):
  body=models.TextField()
  author=models.CharField(max_length=60)
  created=models.DateField()
  updated=models.DateField()
  post=models.ForeignKey(Post)
  
  
  def __unicode__(self):
    return ('%s:%s'%(self.post,self.body[:60]))
def body_first_60(self):
  return self.body[:60]






# Create your models here.
