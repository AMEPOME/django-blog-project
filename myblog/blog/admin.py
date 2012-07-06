from  blog.models import Comment,Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
  list_display=('title','created','updated')
  list_filter = ('title','created')
  search_fields = ('title', 'body')

class CommentAdmin(admin.ModelAdmin):
  list_display=('post','author','body','created','updated')
  list_filter = ('author','created')
class CommentInline(admin.TabularInline):
  model=Comment
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
#admin.site.register(Post)
#admin.site.register(Comment)
