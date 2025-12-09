#!/bin/sh

# This script starts the API server and then runs the data simulator.

python app.py &
sleep 3
python simulator.py
