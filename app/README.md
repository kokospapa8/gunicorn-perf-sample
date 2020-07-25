ENV
```
DB_PASSWORD
DB_HOST
WORKER_COUNT
```
export WORKER_COUNT=5
export TH_COUNT=1
docker-compose -f docker-compose-staging.yml up -d

$ ps aux | grep guni
$ top