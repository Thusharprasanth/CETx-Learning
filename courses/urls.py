from django.urls import path
from . import views



urlpatterns = [
    path('', views.store, name='store'),
    path('course/<slug:category_slug>', views.store, name='course_by_category'),
]