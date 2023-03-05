from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import BasePermission
from django.contrib.auth.hashers import make_password

from .models import CustomUser
from .serializer import CustomUserModelSerializer
from TODO_2.models import TODO, Project, Users
from TODO_2.serializer_2 import TODOModelSerializer, ProjectModelSerializer, UsersModelSerializer
from TODO.filters import ProjectFilter


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class TODOModelViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateAPIView,
                        GenericViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter


class ProjectModelViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateAPIView,
                          GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class UserModelViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateAPIView,
                       GenericViewSet):
    renderer_classes = [AdminRenderer]
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class CustomUserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateAPIView, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff