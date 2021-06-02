from category.models import Category
from courses.models import Course
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Course

# Create your views here.
def store(request, category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=categories, is_available=True)
    else:
        courses = Course.objects.all().filter(is_available=True)
    context = {
        'courses' : courses
    }
    return render(request , 'store/store.html', context)