#!/usr/bin/python3
"""
displays body of response and handles erros
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.agrv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
