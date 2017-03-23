from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import BlogPost, Tags
from .forms import BlogPostForm, BlogPostModelForm
from .services import create_blog_post


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


# def create_new_post(request):
#     form = BlogPostForm()

#     if request.method == 'POST':
#         form = BlogPostForm(data=request.POST)
#         if form.is_valid():
#             # create_blog_post(**form.cleaned_data)
#             return redirect(reverse('index.html'))
#     return render(request, 'create_new_post.html', locals())


def create_new_post(request):
    form = BlogPostModelForm()

    if request.method == 'POST':
        form = BlogPostModelForm(data=request.POST)
        if form.is_valid():
            create_blog_post(**form.cleaned_data)
            return redirect(reverse('index.html'))

    return render(request, 'create_new_post.html', locals())
