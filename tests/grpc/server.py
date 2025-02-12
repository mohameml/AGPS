import grpc
from concurrent import futures
import time
import service_pb2
import service_pb2_grpc

class MyServiceServicer(service_pb2_grpc.MyServiceServicer):
    def SayHello(self, request, context):
        response = service_pb2.ResponseMessage()
        response.message = f"Hello, {request.name}!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("🚀 Server is running on port 50051")
    try:
        while True:
            time.sleep(86400)  # Garde le serveur en vie
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()