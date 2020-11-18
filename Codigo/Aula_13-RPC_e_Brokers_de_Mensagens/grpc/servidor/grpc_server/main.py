import grpc

from concurrent import futures

from grpc_server import blog_pb2 as messages
from grpc_server import blog_pb2_grpc

autor = messages.Autor(nome='Mathias', email='algum conteudo', Posts=[])
post = messages.Post(titulo='Testando gRPC', autor=autor, comments=[])


class PostService(blog_pb2_grpc.PostServiceServicer):

    def ListPosts(self, request, context):
        return messages.PostListReply(posts=[post])


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    blog_pb2_grpc.add_PostServiceServicer_to_server(PostService(), server)

    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
