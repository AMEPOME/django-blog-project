# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 

def post_list(request):
  posts = Post.objects.all()
  t = loader.get_template('blog/post_list.html')
  c = Context({'posts':posts })
  return HttpResponse(t.render(c))

def post_list(request):
    post_list = Post.objects.all()
   
    print type(post_list)
    print post_list
    l=[]
    for a in post_list:
      l.append(a.title)
      l.append(a.body)
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
    return render_to_response('blog/base.html',{})

    
