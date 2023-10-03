#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
using urlib
"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html = response.read()

print("Body Response:")
print("\t- type:", type(html))
print("\t-content:", html)
print("\t- utf8 content", html.decode('utf-8'))
