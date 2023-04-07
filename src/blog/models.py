from django.db import models
from django.utils.text import slugify


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    @property
    def published_string(self):
        if self.published:
            return "L'article est publie"
        return "L'article n'est pas publié"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
