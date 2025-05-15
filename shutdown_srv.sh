#!/bin/bash

# Variables
SSH_USER="username"
SSH_HOST="x.x.x.x"
SSH_PORT="22"
SSH_KEY="/home/user/.ssh/ssh.key"
REMOTE_COMMAND="sudo shutdown -h now"

# SSH and execute command
ssh -p "$SSH_PORT" -i "$SSH_KEY" "$SSH_USER@$SSH_HOST" "$REMOTE_COMMAND"
