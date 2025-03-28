# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pricing.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'pricing.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpricing.proto\x12\x0bgrpc_pricer\"\x95\x02\n\x0cPricingInput\x12$\n\x04past\x18\x01 \x03(\x0b\x32\x16.grpc_pricer.PastLines\x12\x1d\n\x15monitoringDateReached\x18\x02 \x01(\x08\x12\x0c\n\x04time\x18\x03 \x01(\x01\x12)\n\ncurrencies\x18\x04 \x03(\x0b\x32\x15.grpc_pricer.Currency\x12\x1a\n\x12\x64omesticCurrencyId\x18\x05 \x01(\t\x12\"\n\x06\x61ssets\x18\x06 \x03(\x0b\x32\x12.grpc_pricer.Asset\x12\x34\n\x0c\x63orrelations\x18\x07 \x03(\x0b\x32\x1e.grpc_pricer.CorrelationMatrix\x12\x11\n\ttime_grid\x18\x08 \x03(\x01\"\x1a\n\tPastLines\x12\r\n\x05value\x18\x01 \x03(\x01\"@\n\x08\x43urrency\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cinterestRate\x18\x02 \x01(\x01\x12\x12\n\nvolatility\x18\x03 \x01(\x01\"/\n\x05\x41sset\x12\x12\n\ncurrencyId\x18\x01 \x01(\t\x12\x12\n\nvolatility\x18\x02 \x01(\x01\"#\n\x11\x43orrelationMatrix\x12\x0e\n\x06values\x18\x01 \x03(\x01\"Y\n\rPricingOutput\x12\r\n\x05price\x18\x01 \x01(\x01\x12\x0e\n\x06\x64\x65ltas\x18\x02 \x03(\x01\x12\x13\n\x0bpriceStdDev\x18\x03 \x01(\x01\x12\x14\n\x0c\x64\x65ltasStdDev\x18\x04 \x03(\x01\"\x07\n\x05\x45mpty\"\x1a\n\x07ReqInfo\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8d\x01\n\nGrpcPricer\x12G\n\x0ePriceAndDeltas\x12\x19.grpc_pricer.PricingInput\x1a\x1a.grpc_pricer.PricingOutput\x12\x36\n\nHelloWorld\x12\x12.grpc_pricer.Empty\x1a\x14.grpc_pricer.ReqInfob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pricing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PRICINGINPUT']._serialized_start=31
  _globals['_PRICINGINPUT']._serialized_end=308
  _globals['_PASTLINES']._serialized_start=310
  _globals['_PASTLINES']._serialized_end=336
  _globals['_CURRENCY']._serialized_start=338
  _globals['_CURRENCY']._serialized_end=402
  _globals['_ASSET']._serialized_start=404
  _globals['_ASSET']._serialized_end=451
  _globals['_CORRELATIONMATRIX']._serialized_start=453
  _globals['_CORRELATIONMATRIX']._serialized_end=488
  _globals['_PRICINGOUTPUT']._serialized_start=490
  _globals['_PRICINGOUTPUT']._serialized_end=579
  _globals['_EMPTY']._serialized_start=581
  _globals['_EMPTY']._serialized_end=588
  _globals['_REQINFO']._serialized_start=590
  _globals['_REQINFO']._serialized_end=616
  _globals['_GRPCPRICER']._serialized_start=619
  _globals['_GRPCPRICER']._serialized_end=760
# @@protoc_insertion_point(module_scope)
