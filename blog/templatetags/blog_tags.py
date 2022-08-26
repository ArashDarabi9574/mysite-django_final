from os import stat
from unicodedata import category
from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()


@register.simple_tag(name="totalposts")
def totalposts():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.inclusion_tag('blog/blog-popular-post.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_at')[:4]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    category_dict = {}
    for name in categories:
        category_dict[name] = posts.filter(category=name).count()
    return {'categories': category_dict}
@register.inclusion_tag('website/our-blog.html')
def ourblog():
    posts = Post.objects.filter(status=1).order_by('-published_at')[:3]
    return {'posts': posts}

