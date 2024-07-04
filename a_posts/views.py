from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import *
from bs4 import BeautifulSoup
from django.contrib import messages
import requests


def home_view(request):
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'posts': posts})


@login_required
def post_create_view(request):
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            website = requests.get(form.data['url'])
            sourcecode = BeautifulSoup(website.text, 'html.parser')
            
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            
            try:
                image = find_image[0]['content']
            except:
                messages.error(request, '¡La imagen solicitada no está en Flickr!')
                return redirect('post-create')
            
            post.image = image
            
            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            
            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist
            
            post.author = request.user
            
            post.save()
            form.save_m2m()
            return redirect('home')
        
    return render(request, 'a_posts/post_create.html', {'form': form})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Publicación eliminada con éxito.')
        return redirect('home')
        
    return render(request, 'a_posts/post_delete.html', {'post' : post})


@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)
    
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación editada con éxito.')
            return redirect('home')
    
    context = {
        'post': post,
        'form': form,
    }
    
    return render(request, 'a_posts/post_edit.html', context)


@login_required
def post_pague_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'a_posts/post_page.html', {'post': post})