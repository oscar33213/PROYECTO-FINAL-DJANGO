from django.shortcuts import render
from blog.models import Post, Categoria


# Create your views here.

def Vista_Blog(request):
    post = Post.objects.all()
    
    return render (request, 'blog/blog.html',{'posts': post} )


def Categorias(request, categoria_id):
    categoriaFilter = Categorias.objects.get(id=categoria_id) #TODO: ARREGLAR DESPUES:
    posts = Post.objects.filter(categoria = categoriaFilter)
    
    return render (request, "blog/categorias.html", {'categoria': categoriaFilter, 'posts': posts})




    
    

