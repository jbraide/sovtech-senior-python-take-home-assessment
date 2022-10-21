import graphene

# import schema
from api.people.schema import Query as people_query

class Query(people_query, graphene.ObjectType):
    pass
class Mutation(people_query, graphene.ObjectType):
    pass

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)