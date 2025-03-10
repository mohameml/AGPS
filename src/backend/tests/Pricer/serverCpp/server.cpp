#include <iostream>
#include <memory>
#include <string>
#include <vector>

#include <grpcpp/grpcpp.h>
#include "pricing.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using grpc_pricer::GrpcPricer;
using grpc_pricer::PricingInput;
using grpc_pricer::PricingOutput;
using grpc_pricer::Empty;
using grpc_pricer::ReqInfo;

class GrpcPricerServiceImpl final : public GrpcPricer::Service {
    Status PriceAndDeltas(ServerContext* context, const PricingInput* request, PricingOutput* reply) override {
        std::cout << "Received Pricing Request" << std::endl;
    
        // Nombre d'actifs (associés aux deltas)
        int numAssets = request->assets_size() + request->currencies_size() - 1;
        std::cout << "nbAsset =" << numAssets << std::endl;
        
        // Réponse bidon avec price = 100.0 et priceStdDev = 2.0
        reply->set_price(100.0);
        reply->set_pricestddev(2.0);
    
        // Remplir deltas et deltasStdDev avec 0.0
        for (int i = 0; i < numAssets; ++i) {
            reply->add_deltas(0.0);
            reply->add_deltasstddev(0.0);
        }
    
        return Status::OK;
    }
    
    
    Status HelloWorld(ServerContext* context, const Empty* request, ReqInfo* reply) override {
        reply->set_message("Hello from gRPC Pricer Server!");
        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    GrpcPricerServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;

    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();
    return 0;
}