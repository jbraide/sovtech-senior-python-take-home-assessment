import json
from graphene_django.utils.testing import GraphQLTestCase
from .models import Person

# import mixer
from mixer.backend.django import mixer

class PersonUnitTestCase(GraphQLTestCase):

    def setUp(self):
        person_data = {
            'name': 'Joseph Braide',
            'height': '1.77m',
            'mass': '80',
            'gender': 'Male',
            'homeworld': 'Earth',
        }
        self.person1 = Person.objects.create(
            **person_data
        )
        # self.person2 = mixer.blend(Person)
        # self.person3 = mixer.blend(Person)
        # self.person4 = mixer.blend(Person)
        # self.person5 = mixer.blend(Person)
        self.persons = mixer.cycle(3000).blend(Person)

    def test_query_all_persons(self):
        response = self.query(
             '''
            query {
                allPersons{
                    name
                    height
                    mass
                    gender
                    homeworld
                }
            }
            ''',
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_query_single_person(self):
        response = self.query(
             '''
            query {
                person (name: "Joseph Braide"){
                    name
                    homeworld
                }
            }
            ''',
        )

        content = json.loads(response.content)
        # print(content)
        self.assertResponseNoErrors(response)

    def test_query_people_paginated(self):
        response = self.query(
            # '''
            # query peoplePaginated{
            #     peoplePaginated{
            #     totalCount
            #     peoplePaginated {
            #     name
            #     }
            #     }
            # }
            # '''
            '''
            query {
                peoplePaginated(page:1){
                name
                height
                    mass
                    gender
                    homeworld
                }
            }
            '''
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
