#!/bin/bash
# displays status code of the response
curl -s -o /dev/null -l --w "%{http_code}" "$1"
