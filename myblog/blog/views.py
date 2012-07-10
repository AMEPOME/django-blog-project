# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
   
    print type(post_list)
    print post_list
    l=[]
    for a in post_list:
      l.append(a.title)
    return HttpResponse(l)

def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if(showComments):
      out=post.body
    else:
      out=post.title
      return HttpResponse(out)   
    
    
def post_search(request, term):
    pass
    #return HttpResponse() 

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
