# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: svdpp-model-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='svdpp-model-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer.svdpp',
  syntax='proto3',
  serialized_options=_b('B\024SVDppModelParamProto'),
  serialized_pb=_b('\n\x17svdpp-model-param.proto\x12,com.webank.ai.fate.core.mlmodel.buffer.svdpp\"4\n\x03Mat\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06values\x18\x03 \x03(\x05\"\xee\x01\n\x0fSVDppModelParam\x12\x16\n\x0e\x61ggregate_iter\x18\x01 \x01(\x05\x12\x19\n\x11saved_model_bytes\x18\x02 \x01(\x0c\x12\x14\n\x0closs_history\x18\x03 \x03(\x01\x12\x14\n\x0cis_converged\x18\x04 \x01(\x08\x12\x0e\n\x06header\x18\x05 \x03(\t\x12\x10\n\x08user_ids\x18\x06 \x03(\t\x12\x10\n\x08item_ids\x18\x07 \x03(\t\x12H\n\rrating_matrix\x18\x08 \x01(\x0b\x32\x31.com.webank.ai.fate.core.mlmodel.buffer.svdpp.MatB\x16\x42\x14SVDppModelParamProtob\x06proto3')
)




_MAT = _descriptor.Descriptor(
  name='Mat',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.Mat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.Mat.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.Mat.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.Mat.values', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=73,
  serialized_end=125,
)


_SVDPPMODELPARAM = _descriptor.Descriptor(
  name='SVDppModelParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregate_iter', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.aggregate_iter', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saved_model_bytes', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.saved_model_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_history', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.loss_history', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.is_converged', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.header', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_ids', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.user_ids', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.item_ids', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rating_matrix', full_name='com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam.rating_matrix', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=128,
  serialized_end=366,
)

_SVDPPMODELPARAM.fields_by_name['rating_matrix'].message_type = _MAT
DESCRIPTOR.message_types_by_name['Mat'] = _MAT
DESCRIPTOR.message_types_by_name['SVDppModelParam'] = _SVDPPMODELPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mat = _reflection.GeneratedProtocolMessageType('Mat', (_message.Message,), dict(
  DESCRIPTOR = _MAT,
  __module__ = 'svdpp_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.svdpp.Mat)
  ))
_sym_db.RegisterMessage(Mat)

SVDppModelParam = _reflection.GeneratedProtocolMessageType('SVDppModelParam', (_message.Message,), dict(
  DESCRIPTOR = _SVDPPMODELPARAM,
  __module__ = 'svdpp_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.svdpp.SVDppModelParam)
  ))
_sym_db.RegisterMessage(SVDppModelParam)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
