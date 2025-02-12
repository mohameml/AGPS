import grpc
import service_pb2
import service_pb2_grpc

def run():
    # 1. Créer un canal de communication vers le serveur gRPC
    channel = grpc.insecure_channel("localhost:50051")
    
    # 2. Créer un stub client à partir du service généré
    stub = service_pb2_grpc.MyServiceStub(channel)
    
    # 3. Construire la requête
    request = service_pb2.RequestMessage(name="Alice")
    
    # 4. Envoyer la requête et recevoir la réponse
    response = stub.SayHello(request)
    
    print(f"🔹 Réponse du serveur: {response.message}")

if __name__ == "__main__":
    run()