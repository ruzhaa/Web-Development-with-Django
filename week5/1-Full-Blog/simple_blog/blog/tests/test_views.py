from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.factories import BlogPostFactory, TagFactory, CommentFactory
from blog.models import BlogPost, Comment

from faker import Factory

faker = Factory.create()


class ViewsTests(TestCase):
    def setUp(self):
        self.tag = TagFactory()
        self.blog_post = BlogPostFactory()
        self.private_blog_post = BlogPostFactory()
        self.private_blog_post.is_private = True
        self.private_blog_post.save()
        self.client = Client()
        self.user = User.objects.create_user(username=faker.word(), password='Ivoepanda')

    def test_index_view_if_logged_user(self):
        self.assertEqual(2, BlogPost.objects.get_private_posts().count())

    def test_index_view_if_not_logged_user(self):
        self.assertEqual(1, BlogPost.objects.get_public_posts().count())

    # test_show_post_get_method

    def test_show_post_view_get_method(self):
        url = '/show-post/' + self.blog_post.title
        response = self.client.get(url)
        response_post = response.context['post']
        self.assertEqual(self.blog_post.title, response_post.title)
        self.assertEqual(self.blog_post.content, response_post.content)
        self.assertEqual(0, Comment.objects.filter(blog_post=self.blog_post).count())

    def test_show_post_view_add_comment(self):
        self.assertEqual(0, Comment.objects.count())
        url = '/show-post/' + self.blog_post.title
        response = self.client.post(url, data={'email': faker.email(),
                                               'content': faker.text(),
                                               'blog_post': self.blog_post})
        blog_post_comment = Comment.objects.filter(blog_post=self.blog_post)\
                                           .count()
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, blog_post_comment)

    def test_create_new_post_view_if_not_logged_user(self):
        self.client.logout()
        response = self.client.get('/create-new-post/')
        self.assertEqual(302, response.status_code)

    def test_create_new_post_view_if_logged_user(self):
        self.client.login(username=self.user.username, password='Ivoepanda')
        self.assertEqual(2, BlogPost.objects.get_private_posts().count())

        response = self.client.post('/create-new-post/',
                                    data={"title": faker.name(),
                                          "content": faker.word(),
                                          "author": self.user,
                                          "tags": self.tag})
        self.assertEqual(302, response.status_code)
        self.assertEqual(3, BlogPost.objects.get_private_posts().count())

    def test_registration_view_success(self):
        self.assertEqual(1, User.objects.count())
        response = self.client.post('/registration/',
                                    data={"username": faker.word(),
                                          "password": 'pakIvoepanda'})
        self.assertEqual(302, response.status_code)
        self.assertEqual(2, User.objects.count())
        self.assertEqual(2, BlogPost.objects.get_private_posts().count())

    def test_login_view_if_not_logged_user(self):
        response = self.client.get('/login/')
        self.assertEqual(200, response.status_code)

        response_post = self.client.post('/login/',
                                         data={"username": self.user.username,
                                               "password": 'Ivoepanda'})
        self.assertEqual(302, response_post.status_code)
        self.assertEqual(2, BlogPost.objects.get_private_posts().count())

    def tearDown(self):
        self.client.logout()
