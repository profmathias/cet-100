# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import blog_pb2 as blog__pb2


class PostServiceStub(object):
    """posts service

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPosts = channel.unary_unary(
                '/blog.PostService/ListPosts',
                request_serializer=blog__pb2.Empty.SerializeToString,
                response_deserializer=blog__pb2.PostListReply.FromString,
                )


class PostServiceServicer(object):
    """posts service

    """

    def ListPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPosts,
                    request_deserializer=blog__pb2.Empty.FromString,
                    response_serializer=blog__pb2.PostListReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blog.PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """posts service

    """

    @staticmethod
    def ListPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blog.PostService/ListPosts',
            blog__pb2.Empty.SerializeToString,
            blog__pb2.PostListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
