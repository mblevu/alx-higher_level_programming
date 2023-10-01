#!/bin/bash
# displays all methods a server will accept
curl -sl "$1" | grep Allow | cut -d '' -f2-
