from django.shortcuts import render, get_list_or_404
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()  # Buscar todos os posts do banco de dados
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_list_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
