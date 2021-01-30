import grpc
from concurrent import futures

from api.files_pb2_grpc import FilesServicer, add_FilesServicer_to_server
from api.files_pb2 import QueryFileResp


class Files(FilesServicer):
    def QueryFile(self, request, context):
        resp = QueryFileResp(file_name='server file name',
                             file_hash='server file hash')
        print(f'resp:{resp}')
        return resp


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FilesServicer_to_server(Files(), server)
    server.add_insecure_port('[::]:8081')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
