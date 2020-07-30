# api_caching_service
Simple service that provides an intermediate API that is backed by a cache providing access to an online API

```
app->.env
REDIS_IP_ADDRESS='xxx.xxx.xx.xx'
REDIS_PORT=6379
REDIS_USERNAME='xxxxx'
CACHE_EXPIRE_AFTER=2500000

test_webshrinker->.env
CACHE_SERVER_API = "http://xxx.xxx.xx.xx:80/webshrinker/"
WEBSHRINKER_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXX"
WEBSHRINKER_SECRET_KEY = "YYYYYYYYYYYYYYYYYYYY"

docker-compose build
docker-compose up -d
```
