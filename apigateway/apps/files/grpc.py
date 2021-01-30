import grpc

from api.files_pb2_grpc import FilesStub

stub = None


def get_stub():
    if stub:
        return stub
    channel = grpc.insecure_channel('localhost:8081')
    return FilesStub(channel)
