import grpc
from concurrent import futures
from os import getenv

import modules.protobuf.morbius_pb2_grpc as morbius_grpc
import modules.protobuf.morbius_pb2 as morbius_pb
import modules.sentiment as sentiment

class MorbiusGrpcServer(morbius_grpc.MorbiusServiceServicer):
    def Sentiment(self, request, context):
        sentence = request.text or ''
        if sentence == '':
            raise ValueError('input cannot be null')

        # sentiment process 
        model_result, description = sentiment.analyze(sentence)

        return morbius_pb.SentimentResponse(
            model_result=model_result,
            description=description,
            text=sentence
        )

    @staticmethod
    def serve():
        port = getenv('GRPC_PORT') or '50051'
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        morbius_grpc.add_MorbiusServiceServicer_to_server(MorbiusGrpcServer(), server)
        server.add_insecure_port('[::]:'+str(port))
        server.start()
        print("serving grpc server at " + port)

        server.wait_for_termination()