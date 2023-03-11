from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

from .models import TODO, Project, Users
from .serializer_2 import TODOModelSerializer, ProjectModelSerializer, UserModelSerializer
from users.serializer import CustomUserModelSerializer
from users.models import CustomUser



class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    # filterset_fields = ['title']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TODOModelSerializer
        return TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name']


class UserModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


# class TodoFilterViewSet(viewsets.ModelViewSet):
#     queryset = TODO.objects.all()
#     serializer_class = TODOModelSerializer