from django.shortcuts import render, redirect
from .import forms
from .import models

# Create your views here.

def add_post(request):
  if request.method == 'POST':
    form = forms.PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('add_post')
  else:
    form = forms.PostForm()
  return render(request, 'add_post.html', {'form': form})

def edit_post(request, id):
  post = models.Post.objects.get(pk=id)

  if request.method == 'POST':
    form = forms.PostForm(request.POST, instance = post)
    if form.is_valid():
      form.save()
      return redirect('homepage')
  else:
    form = forms.PostForm(instance = post)
  return render(request, 'add_post.html', {'form': form})

def delete_post(request, id):
  post = models.Post.objects.get(pk=id).delete()
  return redirect('homepage')