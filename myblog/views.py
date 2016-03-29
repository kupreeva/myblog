#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone
from myblog.models import Post, Category, Tag
from myblog.forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def post_list(request):#display a list of posts/main page
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    list_of_categories = Category.objects.all()
    return render(request, 'myblog/post_list.html', {'posts': posts,'list_of_categories': list_of_categories})

def post_detail(request, pk):#print post on a separate page
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

def category(request, pk):#displaying all posts for a given category
    cat = get_object_or_404(Category, pk=pk)
    posts_in_category = Post.objects.filter(categories=cat)
    return render(request, 'myblog/category_list.html', {'posts_in_category': posts_in_category, 'cat': cat})

def tag(request, pk):#displaying all posts for a given tag
    t = get_object_or_404(Tag, pk=pk)
    posts_in_tag = Post.objects.filter(tags=t)
    return render(request, 'myblog/tag_list.html',{'posts_in_tag': posts_in_tag, 't': t})

def new_post(request):#creation of new post
    if request.method == "POST":#if the form is completed, we go to post_detail page
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.is_draft == False:
                post.published_date = timezone.now()
            else:#post is draft
                post.published_date = None
            post.save()
            return redirect('myblog.views.post_detail', pk=post.pk)
    else:#want to create a new post, so turn on page post_edit
        form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form': form})

def post_edit(request, pk):#edit an existing post
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('myblog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'myblog/post_edit.html', {'form': form})

def post_draft_list(request):#list of unpublished posts
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'myblog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):#publish a draft
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('myblog.views.post_detail', pk=pk)

def post_remove(request, pk):#delete the post
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('myblog.views.post_list')
