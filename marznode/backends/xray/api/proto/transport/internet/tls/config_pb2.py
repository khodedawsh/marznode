# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/tls/config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#transport/internet/tls/config.proto\x12\x1bxray.transport.internet.tls\"\x91\x02\n\x0b\x43\x65rtificate\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12=\n\x05usage\x18\x03 \x01(\x0e\x32..xray.transport.internet.tls.Certificate.Usage\x12\x15\n\rocsp_stapling\x18\x04 \x01(\x04\x12\x18\n\x10\x63\x65rtificate_path\x18\x05 \x01(\t\x12\x10\n\x08key_path\x18\x06 \x01(\t\x12\x18\n\x10One_time_loading\x18\x07 \x01(\x08\"D\n\x05Usage\x12\x10\n\x0c\x45NCIPHERMENT\x10\x00\x12\x14\n\x10\x41UTHORITY_VERIFY\x10\x01\x12\x13\n\x0f\x41UTHORITY_ISSUE\x10\x02\"\xdf\x03\n\x06\x43onfig\x12\x16\n\x0e\x61llow_insecure\x18\x01 \x01(\x08\x12=\n\x0b\x63\x65rtificate\x18\x02 \x03(\x0b\x32(.xray.transport.internet.tls.Certificate\x12\x13\n\x0bserver_name\x18\x03 \x01(\t\x12\x15\n\rnext_protocol\x18\x04 \x03(\t\x12!\n\x19\x65nable_session_resumption\x18\x05 \x01(\x08\x12\x1b\n\x13\x64isable_system_root\x18\x06 \x01(\x08\x12\x13\n\x0bmin_version\x18\x07 \x01(\t\x12\x13\n\x0bmax_version\x18\x08 \x01(\t\x12\x15\n\rcipher_suites\x18\t \x01(\t\x12\'\n\x1bprefer_server_cipher_suites\x18\n \x01(\x08\x42\x02\x18\x01\x12\x13\n\x0b\x66ingerprint\x18\x0b \x01(\t\x12\x1a\n\x12reject_unknown_sni\x18\x0c \x01(\x08\x12,\n$pinned_peer_certificate_chain_sha256\x18\r \x03(\x0c\x12\x31\n)pinned_peer_certificate_public_key_sha256\x18\x0e \x03(\x0c\x12\x16\n\x0emaster_key_log\x18\x0f \x01(\tBs\n\x1f\x63om.xray.transport.internet.tlsP\x01Z0github.com/xtls/xray-core/transport/internet/tls\xaa\x02\x1bXray.Transport.Internet.Tlsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.tls.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.xray.transport.internet.tlsP\001Z0github.com/xtls/xray-core/transport/internet/tls\252\002\033Xray.Transport.Internet.Tls'
  _globals['_CONFIG'].fields_by_name['prefer_server_cipher_suites']._loaded_options = None
  _globals['_CONFIG'].fields_by_name['prefer_server_cipher_suites']._serialized_options = b'\030\001'
  _globals['_CERTIFICATE']._serialized_start=69
  _globals['_CERTIFICATE']._serialized_end=342
  _globals['_CERTIFICATE_USAGE']._serialized_start=274
  _globals['_CERTIFICATE_USAGE']._serialized_end=342
  _globals['_CONFIG']._serialized_start=345
  _globals['_CONFIG']._serialized_end=824
# @@protoc_insertion_point(module_scope)
