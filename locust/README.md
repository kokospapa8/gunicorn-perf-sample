# Run GUI 
default port - 8089
```
docker-compose up --scale worker=4

```
# Runcommand without gui
```
docker-compose run locust-standalone locust --host http://localhost -f tests/polls.py --no-web --clients 300 --hatch-rate 300 --run-time 10s --only-summary

docker-compose run locust-standalone locust --host http://localhost -f tests/polls.py --no-web --clients 100 --hatch-rate 100 --run-time 60s --only-summary --step-load --step-clients 100 --step-time 20s

```

