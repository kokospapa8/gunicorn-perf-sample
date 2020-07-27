# Environemnt
- DB_PASSWORD
- DB_HOST
- WORKER_COUNT
- TH_COUNT

# Run command on ec2
> docker-compose -f docker-compose-staging.yml up -d

# Push command for ecs
```
 docker build -f config/app/Dockerfile_nginx -t <account_id>.dkr.ecr.us-west-2.amazonaws.com/nginx:latest .
 docker build -f config/app/Dockerfile -t <account_id>.dkr.ecr.us-west-2.amazonaws.com/gunicorn-perftest:latest .
 docker push <account_id>.dkr.ecr.us-west-2.amazonaws.com/nginx:latest
 docker push <account_id>.dkr.ecr.us-west-2.amazonaws.com/gunicorn-perftest:latest

```

