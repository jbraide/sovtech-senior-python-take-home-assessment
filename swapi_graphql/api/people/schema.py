# graphene & dj_graphene
import graphene

# models & type
from api.models import Person
from .types import PersonType


class Query(graphene.ObjectType):
    all_persons = graphene.List(PersonType)
    person = graphene.Field(PersonType, name=graphene.String())

    def resolve_all_persons(self, info, **kwargs):
        return Person.objects.all()

    def resolve_person(self, info, name):
        if not info.context.user.is_authenticated():
            return Person.objects.none()
        else:
            return Person.objects.get(name=name)

# class Mutation(graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)