from urllib import request
from django.shortcuts import render
from .models import Post
from django.views import generic

class post_list(generic.ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-data')[:3]


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/home.html', {'posts' : posts})

class post_detalhe(generic.DetailView):
    model = Post
    template_name = 'blog/post_detalhe.html'

# def post_detalhe(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     return render(request, 'blog/post_detalhe.html', {'post' : post})



