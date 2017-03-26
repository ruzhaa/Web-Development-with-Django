from django.contrib.auth.models import User
from .models import BlogPost, Tags


def check_and_add_tags(new_post, tags):
    list_tags = tags.split(',')
    for tag in list_tags:
        if Tags.objects.filter(tag=tag).exists():
            t = Tags.objects.filter(tag=tag).first()
        else:
            t = Tags.objects.create(tag=tag)
        new_post.tags.add(t)

    new_post.save()
    return new_post


def check_and_add_author(new_post, author):
    if User.objects.filter(username=author).exists():
        author = User.objects.filter(username=author).first()
    else:
        author = User.objects.create(username=author)

    new_post.authors.add(author)
    new_post.save()
    return new_post


def create_blog_post(*, author, title, content, tags=None):
    print(author)
    post = BlogPost.objects.create(title=title, content=content)
    post = check_and_add_tags(post, tags)
    post = check_and_add_author(post, author)

    return post
