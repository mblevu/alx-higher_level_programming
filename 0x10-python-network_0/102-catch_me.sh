#!/bin/bash
#makes request to catch me route
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0.5000/catch_me
