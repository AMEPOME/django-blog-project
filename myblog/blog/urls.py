from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),	
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    #url(r'^posts/search(?P<token>\w+).','blog.views.post_search'),
    url(r'^posts/search/(\.)','blog.views.post_search')
    
    #url(r'^posts/(?P<id>\d+)/((?P<showsearch>.*)/)?$', #'blog.views.post_search'),
    ## add your url here
)

