# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vmess/outbound/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from marznode.backends.xray.api.proto.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!proxy/vmess/outbound/config.proto\x12\x19xray.proxy.vmess.outbound\x1a!common/protocol/server_spec.proto\"@\n\x06\x43onfig\x12\x36\n\x08Receiver\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpointBm\n\x1d\x63om.xray.proxy.vmess.outboundP\x01Z.github.com/xtls/xray-core/proxy/vmess/outbound\xaa\x02\x19Xray.Proxy.Vmess.Outboundb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.vmess.outbound.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.xray.proxy.vmess.outboundP\001Z.github.com/xtls/xray-core/proxy/vmess/outbound\252\002\031Xray.Proxy.Vmess.Outbound'
  _globals['_CONFIG']._serialized_start=99
  _globals['_CONFIG']._serialized_end=163
# @@protoc_insertion_point(module_scope)
