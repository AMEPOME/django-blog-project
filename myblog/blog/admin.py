from  blog.models import Comment,Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
  list_display=('title','created','updated')
  list_filter = ('created',)
  search_fields = ('title', 'body')
  
  #inlines=[CommentInline]
class CommentAdmin(admin.ModelAdmin):
  list_display=('post','author','body','created','updated')
  list_filter = ('author','created')
class CommentInline(admin.TabularInline):
  model=Comment
  max_num=10
  exclude=['title','body']
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
#admin.site.register(Post)

