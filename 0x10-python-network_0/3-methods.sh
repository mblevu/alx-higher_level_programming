#!/bin/bash
# displays all methods a server will accept
curl -sI "$1" | grep Allow | cut -d''-f2-
