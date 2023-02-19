from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import CustomUser
from TODO_2.models import TODO


class CustomUserModelSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'firstname', 'lastname', 'email')


class TODOModelSerializer(ModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'