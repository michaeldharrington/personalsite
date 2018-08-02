from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User


from public.models import Project
from public.serializers import ProjectSerializer, UserSerializer
from rest_framework import generics


class HomeView(TemplateView):
    template_name = 'public/home.html'
    page_name = 'Home'

class AboutView(TemplateView):
    template_name = 'public/about.html'
    page_name = 'About'

class ResView(TemplateView):
    template_name = 'public/resume.html'
    page_name = 'Resume'

class ProjectListView(ListView):

    model = Project

    template_name = 'public/projects.html'

    page_name = 'Projects'
    context_object_name = 'all_projects'

class ProjectView(DetailView):

    queryset = Project.objects.all()

    def get_object(self):
        object = super().get_object()
        object.last_accessed = timezone.now()
        object.save()
        return object

    template_name = 'public/project.html'
    page_name = 'Project'



class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class UserList(generics.ListAPIView):
    quertset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
