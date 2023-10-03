#!/usr/bin/python3
"""
lists 10 most recent commits on a repo
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    request = requests.get(url)
    commit = request.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[1].get("commit").get("author").het("name")))
    except IndexError:
        pass
