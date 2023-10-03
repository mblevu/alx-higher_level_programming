#!/usr/bin/python3
"""
sends post request with an email parameter to url
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    request = requests.post(url, data=email)
    print(requests.text)
