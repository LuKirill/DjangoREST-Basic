import graphene
from graphene_django import DjangoObjectType
from TODO_2.models import TODO, Project, Users


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todo = graphene.List(TODOType)

    def resolve_all_todo(self, info):
        return TODO.objects.all()


class UserType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


schema = graphene.Schema(query=Query)