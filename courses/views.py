from django.db import models
from category.models import Category
from courses.models import Course
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Course
from carts.models import CartItem, Cart
from carts.views import _cart_id

# Create your views here.
def store(request, category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=categories, is_available=True)
        course_count = courses.count()
    else:
        courses = Course.objects.all().filter(is_available=True)
        course_count = courses.count()
    context = {
        'courses' : courses,
        'course_count' : course_count
    }
    return render(request , 'store/store.html', context)

def course_details(request, category_slug, course_slug):
    single_course = Course.objects.get(category__slug = category_slug, slug=course_slug)
    in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), course = single_course).exists()
    context = {
        'single_course' : single_course,
        'in_cart' : in_cart
    }
    return render(request,'store/course_details.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            courses = Course.objects.filter(course_name__icontains = keyword)
            course_count = courses.count()
    context = {
        'courses' : courses,
        'course_count' : course_count
    }
    return render(request, 'store/store.html', context)