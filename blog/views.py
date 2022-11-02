from urllib import request
from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class post_list(generic.ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-data')[:3]

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/home.html', {'posts' : posts})

class post_detalhe(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detalhe.html'

# def post_detalhe(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     return render(request, 'blog/post_detalhe.html', {'post' : post})

class post_new(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = "__all__"

class post_edit(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('titulo', 'conteudo')

class post_delete(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')