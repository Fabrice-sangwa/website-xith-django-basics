from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()


# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    @property
    def published_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article n'est pas publié"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Author(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    wikipedia = models.URLField(blank=True, null=True)

    @property
    def autor_indetity(self):
        return self.firstname, self.lastname


class Book(models.Model):
    title = models.CharField(max_length=40)
    price = models.FloatField(default=False, null=True)
    summary = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category_list = ["Aventure", "Thriller", "Fantastique", "Romance", "Horreur", "Science-fiction"]
    category = models.TextField(blank=True, null=True, default=category_list)
    stock = models.IntegerField(default=0)

    @property
    def book_tile(self):
        return self.title
