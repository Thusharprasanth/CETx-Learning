from django.contrib import admin
from .models import Course
# Register your models here.
class CourseManager(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('course_name',)}
    list_display = ('course_name', 'author', 'category', 'price', 'stock', 'is_available')

    

admin.site.register(Course, CourseManager)
