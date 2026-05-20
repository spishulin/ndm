docker compose build
docker compose up -d
curl -H "X-Forwarded-For: 203.0.113.195, 70.41.3.18, 150.172.238.178" 172.18.0.2
docker logs app -f
