#!/usr/bin/python3
"""
sends request to url and display X-Request-Id header value
"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
print(response.headers.get("X-Request-Id"))
