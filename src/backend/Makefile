PROTO_DIR=protos
OUT_DIR=HedgingEngine/Pricer
PROTO_FILE=$(PROTO_DIR)/pricing.proto

generate_grpc:
	python3 -m grpc_tools.protoc -I $(PROTO_DIR) --python_out=$(OUT_DIR) --grpc_python_out=$(OUT_DIR) $(PROTO_FILE)

clean:
	rm -f $(OUT_DIR)/*_pb2.py $(OUT_DIR)/*_pb2_grpc.py

test:
	python3 -m backend.tests.test_market_reader_exchange_rate
	
