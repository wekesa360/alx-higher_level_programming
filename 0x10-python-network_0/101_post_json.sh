#!/bin/bash
# a script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX POST -h "Content-Type: application/json" -d @"$2" "$1"
