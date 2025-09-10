from django.shortcuts import render, redirect
from posts.models import Post


def home(request):
  post = Post.objects.all()
  return render(request, 'home.html', {'post': post})

