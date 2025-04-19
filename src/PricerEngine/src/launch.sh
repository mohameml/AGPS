#!/bin/bash
export LD_LIBRARY_PATH="$(dirname "$0")/lib:$LD_LIBRARY_PATH"
chmod u+x launch.sh 
./bin/pricing_server
