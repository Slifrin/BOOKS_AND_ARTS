# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import weather_pb2 as weather__pb2


class WeatherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTemperature = channel.unary_unary(
                '/pd.Weather/AddTemperature',
                request_serializer=weather__pb2.Temperature.SerializeToString,
                response_deserializer=weather__pb2.AddReply.FromString,
                )


class WeatherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTemperature(self, request, context):
        """Add temperture reading
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeatherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTemperature,
                    request_deserializer=weather__pb2.Temperature.FromString,
                    response_serializer=weather__pb2.AddReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pd.Weather', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Weather(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pd.Weather/AddTemperature',
            weather__pb2.Temperature.SerializeToString,
            weather__pb2.AddReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
