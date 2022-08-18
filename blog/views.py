from urllib import request
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/home.html', {})


