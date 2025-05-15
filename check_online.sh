#!/bin/bash

URL="https://ismcserver.online/your_minecraft_server"
CHECK_STRING="Online"
WAIT_TIME=10  # Time in seconds to wait before the next check

while true; do
    # Use curl to fetch the content of the URL and grep to search for the string "offline"
    if curl -s "$URL" | grep -q "$CHECK_STRING"; then
        #echo "The string '$CHECK_STRING' was found, exiting."
        exit 0
    else
        #echo "The string '$CHECK_STRING' was not found, waiting..."
        sleep $WAIT_TIME
    fi
done
