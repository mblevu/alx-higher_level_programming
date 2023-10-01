#!/bin/bash
# get url body size
curl -sl "$1" | grep -i Content-Length | awk '{print$2}'
