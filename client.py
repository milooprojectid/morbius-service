from __future__ import print_function
import logging
import grpc
import modules.morbius_pb2 as morbius_pb2
import modules.morbius_pb2_grpc as morbius_pb2_grpc


def run():
    with grpc.insecure_channel('127.0.0.1:6060') as channel:
        stub = morbius_pb2_grpc.MorbiusServiceStub(channel)
        response = stub.Sentiment(morbius_pb2.SentimentRequest(text='dia adalah seseorang yang sangat menawan'))
    print("Client received: " + response.description)


if __name__ == '__main__':
    logging.basicConfig()
    run()