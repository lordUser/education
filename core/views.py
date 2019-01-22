from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from students.models import StudentGroup, Student


@method_decorator(login_required, name='dispatch')
class Home(ListView):
    template_name = 'core/home.html'
    model = StudentGroup


@method_decorator(login_required, name='dispatch')
class Group(ListView):
    template_name = 'core/group.html'

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Student.objects.filter(group=group_id)


class GroupCreate(CreateView):
    model = StudentGroup
    fields = ['name', 'captain']


class GroupUpdate(UpdateView):
    fields = ['name', 'captain']

    def get_object(self):
        group_id = self.kwargs['group_id']
        return get_object_or_404(StudentGroup, id=group_id)


class GroupDelete(DeleteView):
    model = StudentGroup
    success_url = reverse_lazy('core:home')

    def get_object(self):
        group_id = self.kwargs['group_id']
        return get_object_or_404(StudentGroup, id=group_id)


class StudentCreate(CreateView):
    model = Student
    fields = ['first_name', 'second_name', 'last_name', 'birthdate', 'group']


class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'second_name', 'last_name', 'birthdate', 'group']

    def get_object(self):
        student_id = self.kwargs['student_id']
        return get_object_or_404(Student, ticket=student_id)


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('core:home')

    def get_object(self):
        student_id = self.kwargs['student_id']
        return get_object_or_404(Student, ticket=student_id)