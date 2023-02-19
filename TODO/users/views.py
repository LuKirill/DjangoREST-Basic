from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializer import CustomUserModelSerializer
from TODO_2.models import TODO, Project, Users
from TODO_2.serializer_2 import TODOModelSerializer, ProjectModelSerializer, UsersModelSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectModelSerializer(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

  
class UsersModelSerializer(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer