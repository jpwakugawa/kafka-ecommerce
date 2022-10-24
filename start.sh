#!/bin/bash

echo "Starting Kafka..."

docker network create --driver=bridge broker
docker compose up -d
docker compose -f docker-compose.ui.yml up -d

echo "All done!"