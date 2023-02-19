from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import TODO, Project, Users
from .serializer_2 import TODOModelSerializer, ProjectModelSerializer, UsersModelSerializer
from users.serializer import CustomUserModelSerializer
from users.models import CustomUser


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class TODOModelSerializer(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectModelSerializer(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

  
class UsersModelSerializer(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer