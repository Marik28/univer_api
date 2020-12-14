from django.shortcuts import render
from django.views.generic import ListView, DetailView

from schedule.models import Teacher


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
