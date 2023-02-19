from rest_framework.serializers import ModelSerializer
from .models import TODO, Project, Users


class TODOModelSerializer(ModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class UsersModelSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'