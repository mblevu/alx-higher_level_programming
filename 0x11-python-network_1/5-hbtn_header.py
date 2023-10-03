#!/usr/bin/python3
"""
sends request to url and display X-Request-Id header value
"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
x_request_id = response.headers.get("X-Request-Id")

print(x_request_id)
