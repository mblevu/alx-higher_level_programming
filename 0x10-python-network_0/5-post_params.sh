#!/bin/bash
# displays body of response
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=i will alwyas be here for PLD"
