#!/bin/bash

## This is a script that does a ping sweep on the network the device is connected to then runs a port scan on each active host and returns a list of open ports to a file.

## Ping Sweeping
echo "========== Ping sweep in progress... =========="

echo sort | fping -a -g 192.168.1.1 192.168.1.254 > hosts.txt

echo "========== Done ping sweep =========="


## Port Scanning
echo "========== Port scanning in progress...=========="

python hosts.txt

echo "========== Done port scanning =========="