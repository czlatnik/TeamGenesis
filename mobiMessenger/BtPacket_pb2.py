# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BtPacket.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BtPacket.proto',
  package='',
  serialized_pb=_b('\n\x0e\x42tPacket.proto\"P\n\x08\x42tPacket\x12\x0f\n\x07utcTime\x18\x01 \x02(\x04\x12\x12\n\ndeviceName\x18\x02 \x02(\t\x12\x11\n\ttopicName\x18\x03 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BTPACKET = _descriptor.Descriptor(
  name='BtPacket',
  full_name='BtPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utcTime', full_name='BtPacket.utcTime', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='BtPacket.deviceName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topicName', full_name='BtPacket.topicName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='BtPacket.data', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['BtPacket'] = _BTPACKET

BtPacket = _reflection.GeneratedProtocolMessageType('BtPacket', (_message.Message,), dict(
  DESCRIPTOR = _BTPACKET,
  __module__ = 'BtPacket_pb2'
  # @@protoc_insertion_point(class_scope:BtPacket)
  ))
_sym_db.RegisterMessage(BtPacket)


# @@protoc_insertion_point(module_scope)
