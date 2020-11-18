import grpc
from grpc_client import blog_pb2
from grpc_client import blog_pb2_grpc


def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = blog_pb2_grpc.PostServiceStub(channel)
    response = stub.ListPosts(blog_pb2.Empty())

    print(response)


if __name__ == '__main__':
    main()
