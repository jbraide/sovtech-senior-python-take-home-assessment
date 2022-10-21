from graphene_django.types import DjangoObjectType

from api.models import Person

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = [
            'name',
            'height',
            'mass',
            'gender',
            'homeworld',
        ]