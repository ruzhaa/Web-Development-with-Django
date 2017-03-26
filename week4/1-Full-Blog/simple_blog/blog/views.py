from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost, Comment, Tags
from .forms import BlogPostForm, CommentsForm
from .services import create_blog_post
from django.utils import timezone


def index(request):
    all_tags = Tags.objects.all()
    try:
        blog_posts = BlogPost.objects.all()
    except BlogPost.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'index.html', locals())


def show_post(request, title):
    form = CommentsForm()

    post = BlogPost.objects.filter(title=title).first()
    comments = Comment.objects.filter(blog_post=post)
    comments_count = comments.count()

    if request.method == 'POST':
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(author_email=request.POST.get('email'),
                                   created_date=timezone.now(),
                                   content=request.POST.get('content'),
                                   blog_post=post)
            comments_count += 1
    return render(request, 'show_post.html', locals())


def create_new_post(request):
    all_tags = Tags.objects.all()
    form = BlogPostForm()

    if request.method == 'POST':
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            post = create_blog_post(**form.cleaned_data)
            alert = "Well done! You successfully create new blog post."
            return render(request, 'create_new_post.html', {'alert': alert})
    return render(request, 'create_new_post.html', locals())
