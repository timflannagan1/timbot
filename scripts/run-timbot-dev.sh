#! /bin/bash

CONTAINER_RUN_CMD=${CONTAINER_RUN_CMD:-"docker run"}
CONTAINER_ENV_FILE=${CONTAINER_ENV_FILE:-"dev-local-env"}

${CONTAINER_RUN_CMD} \
    --rm \
    -it \
    --network="host" \
    -e SLACK_API_TOKEN="$SLACK_API_TOKEN" \
    -e SLACK_TIMBOT_USER_ID="$SLACK_TIMBOT_USER_ID" \
    -e SLACK_CHANNEL_ID="$SLACK_CHANNEL_ID" \
    -e MYSQL_USER="$MYSQL_USER" \
    -e MYSQL_PASSWORD="$MYSQL_PASSWORD" \
    -e MYSQL_HOST="$MYSQL_HOST" \
    -e MYSQL_DATABASE="$MYSQL_DATABASE" \
    timbot:timbot
