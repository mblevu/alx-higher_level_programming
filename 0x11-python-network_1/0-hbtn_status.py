#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
using urlib
"""


if __name__ == "__main__":
    import urllib.request

    url = 'http://0.0.0.0:5050/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body Response:")
        print("\t- type:".format(type(html)))
        print("\t-content:".format(html))
        print("\t- utf8 content".format(html.decode('utf-8')))
