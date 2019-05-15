
from django.conf.urls import url
from django.urls import path

from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView,CourseListView
app_name = "course"
urlpatterns = [
    path('about/',AboutView.as_view(),name="about"),
    path('course-list/',CourseListView.as_view(),name="course-list"),

     ]
