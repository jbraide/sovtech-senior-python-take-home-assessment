# graphene & dj_graphene
import graphene

# dj imports
from django.db.models import Q

# models & type
from api.models import Person
from .types import PersonType

class Query(graphene.ObjectType):
    all_persons = graphene.List(PersonType)
    person = graphene.Field(PersonType, name=graphene.String())
    people_paginated = graphene.List(
        PersonType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
        page=graphene.Int(),
        )

    def resolve_all_persons(self, info, **kwargs):
        return Person.objects.all()

    def resolve_person(self, info, name):
        return Person.objects.get(name=name)
    
    def resolve_people_paginated(self, info, search=None, first=10, skip=0, page=None, **kwargs):

        qs = Person.objects.all()
        # if search:
        #     filter = (
        #         Q(url__icontains=search) |
        #         Q(description__icontains=search)
        #     )
        #     qs = qs.filter(filter)
        if page > 1:
            next = page * 10
            qs = qs[next:]
        else:
            qs = qs[skip:]
            
        # if skip:
        #     qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs


schema = graphene.Schema(query=Query)