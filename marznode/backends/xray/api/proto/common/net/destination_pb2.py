# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/destination.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from marznode.backends.xray.api.proto.common.net import network_pb2 as common_dot_net_dot_network__pb2
from marznode.backends.xray.api.proto.common.net import address_pb2 as common_dot_net_dot_address__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63ommon/net/destination.proto\x12\x0fxray.common.net\x1a\x18\x63ommon/net/network.proto\x1a\x18\x63ommon/net/address.proto\"q\n\x08\x45ndpoint\x12)\n\x07network\x18\x01 \x01(\x0e\x32\x18.xray.common.net.Network\x12,\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x03 \x01(\rBO\n\x13\x63om.xray.common.netP\x01Z$github.com/xtls/xray-core/common/net\xaa\x02\x0fXray.Common.Netb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.net.destination_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.xray.common.netP\001Z$github.com/xtls/xray-core/common/net\252\002\017Xray.Common.Net'
  _globals['_ENDPOINT']._serialized_start=101
  _globals['_ENDPOINT']._serialized_end=214
# @@protoc_insertion_point(module_scope)
