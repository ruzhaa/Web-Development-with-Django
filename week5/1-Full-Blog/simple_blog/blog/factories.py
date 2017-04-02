import factory
from .models import Tags, BlogPost, Comment
from faker import Factory

faker = Factory.create()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tags

    tag = factory.LazyAttribute(lambda _: faker.word())


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyAttribute(lambda _: faker.word())
    content = factory.LazyAttribute(lambda _: faker.text())
    is_private = faker.boolean(chance_of_getting_true=0)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    auther_email = factory.LazyAttribute(lambda _: faker.email())
    content = factory.LazyAttribute(lambda _: faker.text())
