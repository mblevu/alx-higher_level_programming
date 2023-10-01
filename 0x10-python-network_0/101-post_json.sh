#!/bin/bash
# curls a json file
curl -s -H "content-type:application/json" -d @"$2" -X POST "$1"
