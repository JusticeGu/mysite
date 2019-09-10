from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView,ListView
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateResponseMixin
#from .models import Course,Lesson
from .forms import CreateCourseForm, CreateLessonForm

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from braces.views import LoginRequiredMixin
import json
# Create your views here.
class AboutView(TemplateView):
    template_name = "course/about.html"


class CourseListView(ListView):
    model = Course
    context_object_name = "course"
    template_name = 'course/course_list.html'

class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)

class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = "/account/login/"

class ManageCourseListView(UserCourseMixin, ListView):
    context_object_name = "courses"
    template_name = 'course/manage/manage_course_list.html'
