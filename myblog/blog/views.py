# Create your views here.
from django.template import Context, loader,Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def post_list(request):
  posts = Post.objects.all()
  t = loader.get_template('blog/post_list.html')
  c = Context({'posts':posts })
  return HttpResponse(t.render(c))

class CommentForm(ModelForm):
  class Meta:
    model=Comment
    exclude=['post']
#def get_data(request):
    
     
@csrf_exempt
def post_detail(request, id, showComments=False):
  if request.method == 'POST':	
       form = CommentForm(request.POST)
       if form.is_valid():
          form.save()
       return HttpResponseRedirect(request.path)
  else:
       form = CommentForm()
  post=Post.objects.get(pk=id)
  comments=Comment.objects.filter(post=post)
  #if(showComments):
      #out='<h1>'+post.title+'</h1>'+'<br>'+post.body+'</br>'
  #else:
      #out=post.title+'\n'
  d=dict(post=post,comments=comments,form=CommentForm(),user=request.user)
  d.update((request))
  return render_to_response('blog/post_detail.html',d) 
  
        
      
      
    
    
def post_search(request, term):
    pass
    #return HttpResponse() 

def home(request):
    return render_to_response('blog/base.html',{})
