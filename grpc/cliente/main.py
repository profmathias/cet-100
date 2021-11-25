import grpc
from blog_pb2 import Empty
from blog_pb2_grpc import PostServiceStub


def main():
    channel = grpc.insecure_channel('localhost:50051')
    servicoDePosts = PostServiceStub(channel)
    response = servicoDePosts.ListPosts(Empty())

    print(response)


if __name__ == '__main__':
    main()
