# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/router/command/command.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from marznode.backends.xray.api.proto.common.net import network_pb2 as common_dot_net_dot_network__pb2
from marznode.backends.xray.api.proto.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n app/router/command/command.proto\x12\x17xray.app.router.command\x1a\x18\x63ommon/net/network.proto\x1a!common/serial/typed_message.proto\"\x83\x03\n\x0eRoutingContext\x12\x12\n\nInboundTag\x18\x01 \x01(\t\x12)\n\x07Network\x18\x02 \x01(\x0e\x32\x18.xray.common.net.Network\x12\x11\n\tSourceIPs\x18\x03 \x03(\x0c\x12\x11\n\tTargetIPs\x18\x04 \x03(\x0c\x12\x12\n\nSourcePort\x18\x05 \x01(\r\x12\x12\n\nTargetPort\x18\x06 \x01(\r\x12\x14\n\x0cTargetDomain\x18\x07 \x01(\t\x12\x10\n\x08Protocol\x18\x08 \x01(\t\x12\x0c\n\x04User\x18\t \x01(\t\x12K\n\nAttributes\x18\n \x03(\x0b\x32\x37.xray.app.router.command.RoutingContext.AttributesEntry\x12\x19\n\x11OutboundGroupTags\x18\x0b \x03(\t\x12\x13\n\x0bOutboundTag\x18\x0c \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x1cSubscribeRoutingStatsRequest\x12\x16\n\x0e\x46ieldSelectors\x18\x01 \x03(\t\"\x82\x01\n\x10TestRouteRequest\x12?\n\x0eRoutingContext\x18\x01 \x01(\x0b\x32\'.xray.app.router.command.RoutingContext\x12\x16\n\x0e\x46ieldSelectors\x18\x02 \x03(\t\x12\x15\n\rPublishResult\x18\x03 \x01(\x08\"\"\n\x13PrincipleTargetInfo\x12\x0b\n\x03tag\x18\x01 \x03(\t\"\x1e\n\x0cOverrideInfo\x12\x0e\n\x06target\x18\x02 \x01(\t\"\x8e\x01\n\x0b\x42\x61lancerMsg\x12\x37\n\x08override\x18\x05 \x01(\x0b\x32%.xray.app.router.command.OverrideInfo\x12\x46\n\x10principle_target\x18\x06 \x01(\x0b\x32,.xray.app.router.command.PrincipleTargetInfo\"%\n\x16GetBalancerInfoRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"Q\n\x17GetBalancerInfoResponse\x12\x36\n\x08\x62\x61lancer\x18\x01 \x01(\x0b\x32$.xray.app.router.command.BalancerMsg\"D\n\x1dOverrideBalancerTargetRequest\x12\x13\n\x0b\x62\x61lancerTag\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\" \n\x1eOverrideBalancerTargetResponse\"X\n\x0e\x41\x64\x64RuleRequest\x12\x30\n\x06\x63onfig\x18\x01 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x14\n\x0cshouldAppend\x18\x02 \x01(\x08\"\x11\n\x0f\x41\x64\x64RuleResponse\"$\n\x11RemoveRuleRequest\x12\x0f\n\x07ruleTag\x18\x01 \x01(\t\"\x14\n\x12RemoveRuleResponse\"\x08\n\x06\x43onfig2\xbf\x05\n\x0eRoutingService\x12{\n\x15SubscribeRoutingStats\x12\x35.xray.app.router.command.SubscribeRoutingStatsRequest\x1a\'.xray.app.router.command.RoutingContext\"\x00\x30\x01\x12\x61\n\tTestRoute\x12).xray.app.router.command.TestRouteRequest\x1a\'.xray.app.router.command.RoutingContext\"\x00\x12v\n\x0fGetBalancerInfo\x12/.xray.app.router.command.GetBalancerInfoRequest\x1a\x30.xray.app.router.command.GetBalancerInfoResponse\"\x00\x12\x8b\x01\n\x16OverrideBalancerTarget\x12\x36.xray.app.router.command.OverrideBalancerTargetRequest\x1a\x37.xray.app.router.command.OverrideBalancerTargetResponse\"\x00\x12^\n\x07\x41\x64\x64Rule\x12\'.xray.app.router.command.AddRuleRequest\x1a(.xray.app.router.command.AddRuleResponse\"\x00\x12g\n\nRemoveRule\x12*.xray.app.router.command.RemoveRuleRequest\x1a+.xray.app.router.command.RemoveRuleResponse\"\x00\x42g\n\x1b\x63om.xray.app.router.commandP\x01Z,github.com/xtls/xray-core/app/router/command\xaa\x02\x17Xray.App.Router.Commandb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.router.command.command_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.xray.app.router.commandP\001Z,github.com/xtls/xray-core/app/router/command\252\002\027Xray.App.Router.Command'
  _globals['_ROUTINGCONTEXT_ATTRIBUTESENTRY']._loaded_options = None
  _globals['_ROUTINGCONTEXT_ATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_ROUTINGCONTEXT']._serialized_start=123
  _globals['_ROUTINGCONTEXT']._serialized_end=510
  _globals['_ROUTINGCONTEXT_ATTRIBUTESENTRY']._serialized_start=461
  _globals['_ROUTINGCONTEXT_ATTRIBUTESENTRY']._serialized_end=510
  _globals['_SUBSCRIBEROUTINGSTATSREQUEST']._serialized_start=512
  _globals['_SUBSCRIBEROUTINGSTATSREQUEST']._serialized_end=566
  _globals['_TESTROUTEREQUEST']._serialized_start=569
  _globals['_TESTROUTEREQUEST']._serialized_end=699
  _globals['_PRINCIPLETARGETINFO']._serialized_start=701
  _globals['_PRINCIPLETARGETINFO']._serialized_end=735
  _globals['_OVERRIDEINFO']._serialized_start=737
  _globals['_OVERRIDEINFO']._serialized_end=767
  _globals['_BALANCERMSG']._serialized_start=770
  _globals['_BALANCERMSG']._serialized_end=912
  _globals['_GETBALANCERINFOREQUEST']._serialized_start=914
  _globals['_GETBALANCERINFOREQUEST']._serialized_end=951
  _globals['_GETBALANCERINFORESPONSE']._serialized_start=953
  _globals['_GETBALANCERINFORESPONSE']._serialized_end=1034
  _globals['_OVERRIDEBALANCERTARGETREQUEST']._serialized_start=1036
  _globals['_OVERRIDEBALANCERTARGETREQUEST']._serialized_end=1104
  _globals['_OVERRIDEBALANCERTARGETRESPONSE']._serialized_start=1106
  _globals['_OVERRIDEBALANCERTARGETRESPONSE']._serialized_end=1138
  _globals['_ADDRULEREQUEST']._serialized_start=1140
  _globals['_ADDRULEREQUEST']._serialized_end=1228
  _globals['_ADDRULERESPONSE']._serialized_start=1230
  _globals['_ADDRULERESPONSE']._serialized_end=1247
  _globals['_REMOVERULEREQUEST']._serialized_start=1249
  _globals['_REMOVERULEREQUEST']._serialized_end=1285
  _globals['_REMOVERULERESPONSE']._serialized_start=1287
  _globals['_REMOVERULERESPONSE']._serialized_end=1307
  _globals['_CONFIG']._serialized_start=1309
  _globals['_CONFIG']._serialized_end=1317
  _globals['_ROUTINGSERVICE']._serialized_start=1320
  _globals['_ROUTINGSERVICE']._serialized_end=2023
# @@protoc_insertion_point(module_scope)
