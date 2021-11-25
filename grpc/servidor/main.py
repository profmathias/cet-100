import grpc
from concurrent import futures

from blog_pb2 import Autor, Post, PostListReply
import blog_pb2_grpc

autor = Autor(nome='Mathias',
              email='alguma@coisa.com',
              Posts=[])
post1 = Post(titulo='Testando gRPC', autor=autor, comments=[])
post2 = Post(titulo='Testando2 gRPC2', autor=autor, comments=[])


class PostService(blog_pb2_grpc.PostServiceServicer):

    def ListPosts(self, request, context):
        return PostListReply(posts=[post1, post2])


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    blog_pb2_grpc.add_PostServiceServicer_to_server(PostService(), server)

    print("iniciando serviço...")
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
