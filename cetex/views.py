from courses.models import Course
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses
    }
    return render(request , 'index.html', context)