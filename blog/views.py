from atexit import register
import datetime
from pickle import NONE
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(response, cat_name=None, author_username=None, **kwargs):
    posts = Post.objects.filter(status=1,published_at__lte=datetime.datetime.now()).order_by('-created_at')
    if author_username:
        posts = posts.filter(author__username=author_username)
    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)
    try:
        page_num = response.GET.get('page')
        posts = posts.get_page(page_num)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(response, 'blog/blog-home.html', context)


def blog_single_view(response, pid):
    posts = Post.objects.filter(status=1, published_at__lte=datetime.datetime.now()).order_by('-created_at')
    post = get_object_or_404(posts, pk=pid, status=1)
    post.content_view += 1
    post.save()
    nextpost = Post.objects.filter(id__gt=post.pk).order_by('pk').first()
    prevpost = Post.objects.filter(id__lt=post.pk).order_by('pk').last()
    context = {'post': post, 'nextpost': nextpost, 'prevpost': prevpost}

    return render(response, 'blog/blog-single.html', context)


def search_view(response):
    posts = Post.objects.filter(status=1)
    if response.method == 'GET':
        if s := response.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(response, 'blog/blog-home.html', context)
