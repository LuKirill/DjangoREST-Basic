from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .models import TODO, Project, Users
from .serializer_2 import TODOModelSerializer, ProjectModelSerializer, UsersModelSerializer
from users.serializer import CustomUserModelSerializer
from users.models import CustomUser


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset_fields = ['title']


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name']

  
class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer


class TodoFilterViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer