echo "Starting Kafka..."
docker network create --driver=bridge broker
docker compose up -d