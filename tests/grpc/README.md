### Étapes détaillées pour configurer et créer un client gRPC en Python  

gRPC (Google Remote Procedure Call) est un framework qui permet la communication entre services via HTTP/2 en utilisant la sérialisation **Protocol Buffers (protobufs)**.  

---

## 🔹 **1. Installer gRPC et Protobufs**  
Avant de commencer, installe les bibliothèques nécessaires :  

```sh
pip install grpcio grpcio-tools protobuf
```

- `grpcio` : Bibliothèque principale gRPC.
- `grpcio-tools` : Outil pour compiler les fichiers `.proto` en Python.
- `protobuf` : Librairie pour la sérialisation des messages.

---

## 🔹 **2. Définir le fichier `.proto` (Définition du service)**  
Créons un fichier `service.proto` qui définit une simple API :  

```proto
syntax = "proto3";

package myservice;

// Définition du message de requête
message RequestMessage {
  string name = 1;
}

// Définition du message de réponse
message ResponseMessage {
  string message = 1;
}

// Définition du service
service MyService {
  rpc SayHello (RequestMessage) returns (ResponseMessage);
}
```

Explication :
- On définit un **service** `MyService` avec une **méthode RPC** `SayHello`.
- `SayHello` prend un `RequestMessage` et renvoie un `ResponseMessage`.

---

## 🔹 **3. Compiler le fichier `.proto` en Python**  
Exécute la commande suivante pour générer le code client et serveur :  

```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
```

- `--python_out=.` → Génère les classes Python pour les messages.
- `--grpc_python_out=.` → Génère les classes gRPC pour le service.

Cela crée deux fichiers :
1. `service_pb2.py` (messages Protobuf)
2. `service_pb2_grpc.py` (stub gRPC pour l'appel distant)

---

## 🔹 **4. Implémenter le serveur gRPC (Juste pour tester le client)**  
Avant d'écrire le client, mettons en place un serveur simple (`server.py`) :

```python
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
```

- Ce serveur écoute sur **port 50051** et implémente la méthode `SayHello`.
- Il utilise un **ThreadPoolExecutor** pour gérer plusieurs requêtes simultanément.

**Lance le serveur en premier :**  
```sh
python server.py
```

---

## 🔹 **5. Implémenter le client gRPC**  
Créons le fichier `client.py` pour appeler le serveur :

```python
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
```

### Explication :
1. **Connexion au serveur gRPC** via `grpc.insecure_channel("localhost:50051")`.
2. **Création d'un stub client** (`MyServiceStub`) qui permet d'appeler les méthodes RPC.
3. **Construction du message de requête** (`RequestMessage(name="Alice")`).
4. **Appel distant de `SayHello`** et récupération de la réponse.
5. **Affichage du message reçu**.

**Lance le client en second :**  
```sh
python client.py
```

---

## ✅ **Conclusion**
Tu as maintenant un **client gRPC fonctionnel** en Python 🎉 !  

### Récapitulatif des étapes :
1. **Installer gRPC** (`pip install grpcio grpcio-tools protobuf`)
2. **Créer un fichier `.proto`** (définition du service)
3. **Compiler le fichier `.proto`** (`grpc_tools.protoc`)
4. **Créer un serveur gRPC** (`server.py`)
5. **Créer un client gRPC** (`client.py`)
6. **Tester la communication** (`python server.py` puis `python client.py`)

Tu veux ajouter une sécurité TLS ou un client asynchrone ? 😊