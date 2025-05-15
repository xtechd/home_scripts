#!/bin/bash

URL="https://ismcserver.online/your_minecraft_server"
STATUS=""

if curl -s "$URL" | grep -q "Online"; then
    STATUS="Online"
else
    STATUS="Offline"
fi

echo "$STATUS"
