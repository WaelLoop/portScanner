#!/bin/bash

## This is a script that does a ping sweep on the network the device is connected to then runs a port scan on each active host and returns a list of open ports to a file.

## Ping Sweeping
echo "========== Ping sweep in progress... =========="

#Fetch the network of the device that is connected
NETWORK=`ifconfig | grep "inet " | grep -v 127.0.0.1 | cut -d\  -f2 | cut -d. -f1-3`
echo sort | fping -a -g "$NETWORK".1 "$NETWORK".254 > hosts.txt

echo "========== Done ping sweep =========="


## Port Scanning
echo "========== Port scanning in progress...=========="

python portScanner.py hosts.txt

echo "========== Done port scanning =========="
