from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()  # Buscar todos os posts do banco de dados
    return render(request, 'blog/post_list.html', {'posts': posts})
