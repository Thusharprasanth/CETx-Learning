from category.models import Category
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/courses')
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
