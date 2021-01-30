import graphene

from api.files_pb2 import QueryFileReq
from apps.files.grpc import get_stub


class File(graphene.ObjectType):
    file_name = graphene.String()
    file_hash = graphene.String()
    file_size = graphene.Int()


class Query(graphene.ObjectType):

    file = graphene.Field(File, file_name=graphene.String(),
                          file_hash=graphene.String())

    def resolve_file(self, info, **kwargs):
        resp = get_stub().QueryFile(QueryFileReq(**kwargs))
        return File(file_name=resp.file_name,
                    file_hash=resp.file_hash, file_size=resp.file_size)


schema = graphene.Schema(query=Query)
