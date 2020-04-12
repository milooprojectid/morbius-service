from dotenv import load_dotenv
from os import path
from modules.server.grpc_server import MorbiusGrpcServer

if __name__ == '__main__':
    load_dotenv(path.join(path.dirname(__file__), '.env'))
    MorbiusGrpcServer.serve()