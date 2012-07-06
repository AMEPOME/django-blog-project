from django.contrib import admin
from django.db import models
def author_60(self):
  return self.author[:60]

class Post(models.Model):
  title=models.CharField(max_length=100)
  body=models.TextField()
  created=models.DateField()
  updated=models.DateField()
  def __unicode__(self):
    return self.title

class PostAdmin(admin.ModelAdmin):
  list_display=('title','created','update')
  list_filter = ('title','created')
  search_fields = ('title', 'body')

class Comment(models.Model):
  body=models.TextField()
  author=models.CharField(max_length=60)
  created=models.DateField()
  updated=models.DateField()
  post=models.ForeignKey(Post)
  def __unicode__(self):
    return self.author

class CommentAdmin(admin.ModelAdmin):
  list_display=('post','author_60','body','created','update')
  list_filter = ('author','created')

class CommentInline(admin.TabularInline):
  model='comment'
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)





# Create your models here.
