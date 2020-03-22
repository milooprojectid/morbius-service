import grpc
import modules.morbius_pb2_grpc as morbius_grpc
import modules.morbius_pb2 as morbius_pb

import pickle
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

from concurrent import futures
from os import getenv

MODEL = load_model('./models/sentiment.h5')
TOKENIZER = pickle.load(open('./models/tokenizer.pkl','rb'))
CLASS_NAME = ['positive', 'neutral', 'negative']

class MorbiusGrpcServer(morbius_grpc.MorbiusServiceServicer):
    def Sentiment(self, request, context):
        sentence = request.text or ''
        if sentence == '':
            raise ValueError('input cannot be null')

        tokenized = TOKENIZER.texts_to_sequences([sentence])
        sequences = pad_sequences(tokenized, maxlen=100, padding='pre', truncating='pre')

        model_result = int(MODEL.predict_classes(sequences))
        description = CLASS_NAME[model_result]

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