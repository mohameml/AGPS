#include <iostream>
#include <string>
#include <fstream>

#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

#include "pnl/pnl_matrix.h"
#include "pricing.grpc.pb.h"
#include "pricing.pb.h"
#include "MonteCarlo.hpp"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;

PnlMat* convertPastToPnlMat(const grpc_pricer::PricingInput& input) {
    // Find size
    int m, n;
    m = input.past_size();
    if (m == 0) {
        return NULL;
    }
    n = input.past(0).value_size();
    for (int i = 0; i < input.past_size(); i++) {
        const grpc_pricer::PastLines &pastLine = input.past(i);
        if (pastLine.value_size() != n) {
            std::cerr << "size mismatch in past" << std::endl;
            return NULL;
        }
    }
    // Parse data
    PnlMat *past = pnl_mat_create(m, n);
    for (int i = 0; i < input.past_size(); i++) {
        const grpc_pricer::PastLines &pastLine = input.past(i);
        for (int j = 0; j < pastLine.value_size(); j++) {
            MLET(past, i, j) = pastLine.value(j);
        }
    }
    return past;
}

// Logic and data behind the server's behavior.
class GrpcPricerImpl final : public grpc_pricer::GrpcPricer::Service {
public:
    GrpcPricerImpl() {}

    Status PriceAndDeltas(ServerContext* context, const grpc_pricer::PricingInput* input, grpc_pricer::PricingOutput* output) override {
        double price, priceStdDev;
        PnlVect *delta = pnl_vect_create(0); // Initialiser avec une taille appropriée
        PnlVect *deltaStdDev = pnl_vect_create(0); // Initialiser avec une taille appropriée
        bool isMonitoringDate = input->monitoringdatereached();
        double currentDate = input->time();
        PnlMat *past = convertPastToPnlMat(*input);
        MonteCarlo Pricer = MonteCarlo(*input);

        if (past == NULL) {
            return Status(grpc::StatusCode::INVALID_ARGUMENT, "Cannot read past");
        }
        std::cout << "========== t = " << input->time() << "===========" << std::endl;
        pnl_mat_print(past);
        Pricer.priceAndDelta(currentDate, past, price, priceStdDev, delta, deltaStdDev);
        output->set_price(price);
        output->set_pricestddev(priceStdDev);
        for (int i = 0; i < delta->size; i++) {
            output->add_deltas(GET(delta, i));
            output->add_deltasstddev(GET(deltaStdDev, i));
        }

        std::cout << "price = " << price << std::endl;
        std::cout << "priceStdDev = " << priceStdDev << std::endl;
        std::cout << "Deltas = ";
        pnl_vect_print_asrow(delta);
        std::cout << "DeltasStdDev  = ";
        pnl_vect_print_asrow(deltaStdDev);

        pnl_mat_free(&past);
        pnl_vect_free(&delta);
        pnl_vect_free(&deltaStdDev);
        return Status::OK;
    }

    Status HelloWorld(ServerContext* context, const grpc_pricer::Empty* input, grpc_pricer::ReqInfo* output) override {
        output->set_message("Hello from server");
        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    GrpcPricerImpl service;

    grpc::EnableDefaultHealthCheckService(true);
    grpc::reflection::InitProtoReflectionServerBuilderPlugin();
    ServerBuilder builder;
    // Listen on the given address without any authentication mechanism.
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    // Register "service" as the instance through which we'll communicate with clients.
    builder.RegisterService(&service);
    // Finally assemble the server.
    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;

    // Wait for the server to shutdown.
    server->Wait();
}

int main(int argc, char **argv) {
    RunServer();
    return 0;
}
