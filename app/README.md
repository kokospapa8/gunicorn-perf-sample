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


docker build -f config/app/Dockerfile_nginx -t 982947632035.dkr.ecr.us-west-2.amazonaws.com/nginx:latest .
docker build -f config/app/Dockerfile -t 982947632035.dkr.ecr.us-west-2.amazonaws.com/gunicorn-perftest:latest .
docker push 982947632035.dkr.ecr.us-west-2.amazonaws.com/nginx:latest

docker push 982947632035.dkr.ecr.us-west-2.amazonaws.com/gunicorn-perftest:latest

