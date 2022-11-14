# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OneHotEncoder.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import DataStructures_pb2 as DataStructures__pb2

try:
  FeatureTypes__pb2 = DataStructures__pb2.FeatureTypes__pb2
except AttributeError:
  FeatureTypes__pb2 = DataStructures__pb2.FeatureTypes_pb2

from .DataStructures_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='OneHotEncoder.proto',
  package='CoreML.Specification',
  syntax='proto3',
  serialized_pb=_b('\n\x13OneHotEncoder.proto\x12\x14\x43oreML.Specification\x1a\x14\x44\x61taStructures.proto\"\xb5\x02\n\rOneHotEncoder\x12>\n\x10stringCategories\x18\x01 \x01(\x0b\x32\".CoreML.Specification.StringVectorH\x00\x12<\n\x0fint64Categories\x18\x02 \x01(\x0b\x32!.CoreML.Specification.Int64VectorH\x00\x12\x14\n\x0coutputSparse\x18\n \x01(\x08\x12H\n\rhandleUnknown\x18\x0b \x01(\x0e\x32\x31.CoreML.Specification.OneHotEncoder.HandleUnknown\"6\n\rHandleUnknown\x12\x12\n\x0e\x45rrorOnUnknown\x10\x00\x12\x11\n\rIgnoreUnknown\x10\x01\x42\x0e\n\x0c\x43\x61tegoryTypeB\x02H\x03P\x00\x62\x06proto3')
  ,
  dependencies=[DataStructures__pb2.DESCRIPTOR,],
  public_dependencies=[DataStructures__pb2.DESCRIPTOR,])



_ONEHOTENCODER_HANDLEUNKNOWN = _descriptor.EnumDescriptor(
  name='HandleUnknown',
  full_name='CoreML.Specification.OneHotEncoder.HandleUnknown',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ErrorOnUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IgnoreUnknown', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=307,
  serialized_end=361,
)
_sym_db.RegisterEnumDescriptor(_ONEHOTENCODER_HANDLEUNKNOWN)


_ONEHOTENCODER = _descriptor.Descriptor(
  name='OneHotEncoder',
  full_name='CoreML.Specification.OneHotEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringCategories', full_name='CoreML.Specification.OneHotEncoder.stringCategories', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64Categories', full_name='CoreML.Specification.OneHotEncoder.int64Categories', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputSparse', full_name='CoreML.Specification.OneHotEncoder.outputSparse', index=2,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='handleUnknown', full_name='CoreML.Specification.OneHotEncoder.handleUnknown', index=3,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ONEHOTENCODER_HANDLEUNKNOWN,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='CategoryType', full_name='CoreML.Specification.OneHotEncoder.CategoryType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=68,
  serialized_end=377,
)

_ONEHOTENCODER.fields_by_name['stringCategories'].message_type = DataStructures__pb2._STRINGVECTOR
_ONEHOTENCODER.fields_by_name['int64Categories'].message_type = DataStructures__pb2._INT64VECTOR
_ONEHOTENCODER.fields_by_name['handleUnknown'].enum_type = _ONEHOTENCODER_HANDLEUNKNOWN
_ONEHOTENCODER_HANDLEUNKNOWN.containing_type = _ONEHOTENCODER
_ONEHOTENCODER.oneofs_by_name['CategoryType'].fields.append(
  _ONEHOTENCODER.fields_by_name['stringCategories'])
_ONEHOTENCODER.fields_by_name['stringCategories'].containing_oneof = _ONEHOTENCODER.oneofs_by_name['CategoryType']
_ONEHOTENCODER.oneofs_by_name['CategoryType'].fields.append(
  _ONEHOTENCODER.fields_by_name['int64Categories'])
_ONEHOTENCODER.fields_by_name['int64Categories'].containing_oneof = _ONEHOTENCODER.oneofs_by_name['CategoryType']
DESCRIPTOR.message_types_by_name['OneHotEncoder'] = _ONEHOTENCODER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OneHotEncoder = _reflection.GeneratedProtocolMessageType('OneHotEncoder', (_message.Message,), dict(
  DESCRIPTOR = _ONEHOTENCODER,
  __module__ = 'OneHotEncoder_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.OneHotEncoder)
  ))
_sym_db.RegisterMessage(OneHotEncoder)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
