#!/usr/bin/python3
"""
send a request to a URL and display value of X-Request_Id
"""
import urllib.request
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.getheader('X-Request-Id')
        print(header)
