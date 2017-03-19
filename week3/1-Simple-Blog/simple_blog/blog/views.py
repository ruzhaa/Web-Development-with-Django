from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost, Tags
from .exceptions import TitleAlreadyExist


def index(request):
    try:
        blog_posts = BlogPost.objects.all()
    except BlogPost.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'index.html', locals())


def show_post(request, title):
    blog_posts = BlogPost.objects.filter(title=title)
    return render(request, 'show_post.html', locals())


def check_and_add_tags(new_post, tag):
    if Tags.objects.filter(tag=tag).exists():
        t = Tags.objects.filter(tag=tag).first()
        new_post.tags.add(t)
    else:
        t = Tags.objects.create(tag=tag)
        new_post.tags.add(t)
    new_post.save()
    return new_post


def create_new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        list_tags = tags.split(',')

        if BlogPost.objects.filter(title=title).exists():
            raise TitleAlreadyExist
        else:
            new_post = BlogPost.objects.create(title=title, content=content)
            for tag in list_tags:
                new_post = check_and_add_tags(new_post, tag)

    return render(request, 'create_new_post.html')
