from django.shortcuts import render, get_object_or_404
from .models import Post
from django.template import RequestContext
from .forms import PageCreate

# Create your views here.
def post(request):
    proyectos= Post.objects.all()
    return render(request,"paginas/post.html",{'proyectos':proyectos})

def detalle(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "paginas/detalle.html", {'detalle':post})

def post_new(request):
     proyectos= Post.objects.all()
     if request.method=="POST":
          form = PageCreate(request.POST)
          if form.is_valid():
            post=form.save(commit=False)
            post.Titulo=request.user
            post.save()
            return render(request,'paginas/post.html',{'proyectos':proyectos})
    
     else:
            form= PageCreate()
            return render(request,"paginas/post_form.html",{'form':form})

def post_detalle(request,id):
     post = get_object_or_404(Post, id=id)
     if request.method=="POST":
          form = PageCreate(request.POST, instance=post)
          if form.is_valid():
            post=form.save(commit=False)
            post.Titulo=request.user
            post.save()
            return render(request, "paginas/detalle.html", {'detalle':post})
    
     else:
            form= PageCreate(instance=post)
            return render(request,"paginas/post_form.html",{'form':form})
    