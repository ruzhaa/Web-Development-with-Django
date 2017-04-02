from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.factories import BlogPostFactory, TagFactory
from blog.models import BlogPost

from faker import Factory

faker = Factory.create()


class QuerySetTests(TestCase):
    def setUp(self):
        self.tag = TagFactory()
        self.blog_post = BlogPostFactory()
        self.client = Client()
        self.user = User.objects.create_user(username=faker.name(), password='Ivoepanda')

    def test_blog_post_public_queryset(self):
        self.assertEqual(self.blog_post, BlogPost.objects.get_public_posts().first())

    def test_blog_post_private_queryset(self):
        self.assertEqual(self.blog_post, BlogPost.objects.get_private_posts().first())

    def test_blog_post_public_queryset_if_not_logged_user(self):
        self.assertEqual(1, BlogPost.objects.count())

        response = self.client.post('/create-new-post/',
                                    data={"title": faker.name(),
                                          "content": faker.word()})
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, BlogPost.objects.count())

    def test_blog_post_public_queryset_with_logged_user(self):
        self.assertEqual(1, BlogPost.objects.count())
        self.client.login(username=self.user.username, password='Ivoepanda')
        response = self.client.post('/create-new-post/',
                                    data={"title": faker.name(),
                                          "content": faker.word(),
                                          "author": self.user,
                                          "tags": self.tag})
        self.assertEqual(self.blog_post, BlogPost.objects.get_public_posts().first())
        self.assertEqual(302, response.status_code)
        self.assertEqual(2, BlogPost.objects.count())

    def test_blog_post_private_queryset_if_not_logged_user(self):
        self.assertEqual(1, BlogPost.objects.count())

        response = self.client.post('/create-new-post/',
                                    data={"title": faker.name(),
                                          "content": faker.word()})
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, BlogPost.objects.count())

    def test_blog_post_private_queryset_with_logged_user(self):
        self.assertEqual(1, BlogPost.objects.count())
        self.client.login(username=self.user.username, password='Ivoepanda')
        response = self.client.post('/create-new-post/',
                                    data={"title": faker.name(),
                                          "content": faker.word(),
                                          "author": self.user,
                                          "tags": self.tag})
        self.assertEqual(self.blog_post, BlogPost.objects.get_private_posts().first())
        self.assertEqual(302, response.status_code)
        self.assertEqual(2, BlogPost.objects.count())

    def tearDown(self):
        self.client.logout()
