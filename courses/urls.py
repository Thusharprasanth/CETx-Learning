from django.urls import path
from . import views



urlpatterns = [
    path('', views.store, name='store'),
    path('course/<slug:category_slug>', views.store, name='course_by_category'),
    path('course/<slug:category_slug>/<slug:course_slug>', views.course_details, name='course_details'),
]