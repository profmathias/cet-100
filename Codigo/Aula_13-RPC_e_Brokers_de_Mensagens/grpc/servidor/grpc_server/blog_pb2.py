# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blog.proto',
  package='blog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nblog.proto\x12\x04\x62log\"\x07\n\x05\x45mpty\"3\n\x05\x41utor\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\r\n\x05Posts\x18\x03 \x03(\t\"6\n\x07\x43omment\x12\x19\n\x11\x61utorDoComentario\x18\x01 \x01(\t\x12\x10\n\x08\x63onteudo\x18\x02 \x01(\t\"S\n\x04Post\x12\x0e\n\x06titulo\x18\x01 \x01(\t\x12\x1a\n\x05\x61utor\x18\x02 \x01(\x0b\x32\x0b.blog.Autor\x12\x1f\n\x08\x63omments\x18\x03 \x03(\x0b\x32\r.blog.Comment\"*\n\rPostListReply\x12\x19\n\x05posts\x18\x01 \x03(\x0b\x32\n.blog.Post2>\n\x0bPostService\x12/\n\tListPosts\x12\x0b.blog.Empty\x1a\x13.blog.PostListReply\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='blog.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=27,
)


_AUTOR = _descriptor.Descriptor(
  name='Autor',
  full_name='blog.Autor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='blog.Autor.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='blog.Autor.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Posts', full_name='blog.Autor.Posts', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=80,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='blog.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='autorDoComentario', full_name='blog.Comment.autorDoComentario', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conteudo', full_name='blog.Comment.conteudo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=136,
)


_POST = _descriptor.Descriptor(
  name='Post',
  full_name='blog.Post',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='titulo', full_name='blog.Post.titulo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autor', full_name='blog.Post.autor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comments', full_name='blog.Post.comments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=221,
)


_POSTLISTREPLY = _descriptor.Descriptor(
  name='PostListReply',
  full_name='blog.PostListReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='posts', full_name='blog.PostListReply.posts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=265,
)

_POST.fields_by_name['autor'].message_type = _AUTOR
_POST.fields_by_name['comments'].message_type = _COMMENT
_POSTLISTREPLY.fields_by_name['posts'].message_type = _POST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Autor'] = _AUTOR
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['Post'] = _POST
DESCRIPTOR.message_types_by_name['PostListReply'] = _POSTLISTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.Empty)
  })
_sym_db.RegisterMessage(Empty)

Autor = _reflection.GeneratedProtocolMessageType('Autor', (_message.Message,), {
  'DESCRIPTOR' : _AUTOR,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.Autor)
  })
_sym_db.RegisterMessage(Autor)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), {
  'DESCRIPTOR' : _COMMENT,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.Comment)
  })
_sym_db.RegisterMessage(Comment)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), {
  'DESCRIPTOR' : _POST,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.Post)
  })
_sym_db.RegisterMessage(Post)

PostListReply = _reflection.GeneratedProtocolMessageType('PostListReply', (_message.Message,), {
  'DESCRIPTOR' : _POSTLISTREPLY,
  '__module__' : 'blog_pb2'
  # @@protoc_insertion_point(class_scope:blog.PostListReply)
  })
_sym_db.RegisterMessage(PostListReply)



_POSTSERVICE = _descriptor.ServiceDescriptor(
  name='PostService',
  full_name='blog.PostService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=267,
  serialized_end=329,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListPosts',
    full_name='blog.PostService.ListPosts',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_POSTLISTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSTSERVICE)

DESCRIPTOR.services_by_name['PostService'] = _POSTSERVICE

# @@protoc_insertion_point(module_scope)
