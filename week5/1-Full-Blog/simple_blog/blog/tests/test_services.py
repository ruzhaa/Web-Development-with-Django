from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.factories import BlogPostFactory, TagFactory
from blog.models import BlogPost

from faker import Factory

faker = Factory.create()


class ServicesTests(TestCase):
    def setUp(self):
        self.tag = TagFactory()
        self.blog_post = BlogPostFactory()
        self.client = Client()
        self.user = User.objects.create_user(username=faker.name(), password='Ivoepanda')

    def test_create_new_post_service_if_not_logged_user(self):
        self.client.logout()
        response = self.client.get('/create-new-post/')
        self.assertEqual(302, response.status_code)

    def test_create_new_post_service_if_logged_user(self):
        self.client.login(username=self.user.username, password='Ivoepanda')
        self.assertEqual(1, BlogPost.objects.get_private_posts().count())

        response = self.client.post('/create-new-post/',
                                    data={"title": faker.name(),
                                          "content": faker.word(),
                                          "author": self.user,
                                          "tags": self.tag})
        self.assertEqual(302, response.status_code)
        self.assertEqual(2, BlogPost.objects.get_private_posts().count())

    def tearDown(self):
        self.client.logout()
