from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import BlogPost, Comment, Tags
from .forms import BlogPostForm, CommentsForm, RegistrationForm
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


def registration_view(request):
    all_tags = Tags.objects.all()
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)

            return redirect(reverse('index'))
        else:
            alert = form.errors
            return render(request, 'registration.html', {'alert': alert})
    return render(request, 'registration.html', locals())


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
        else:
            alert = form.errors
            return render(request, 'login.html', {'alert': alert})
    return render(request, 'login.html', locals())


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))
