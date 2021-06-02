from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField( max_length=30, unique=True)
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('course_by_category', args=['self.slug'])

    def __str__(self):
        return self.category_name