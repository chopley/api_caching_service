# api_caching_service
Simple service that provides an intermediate API that is backed by a cache providing access to an online API

To set up the cache you add an .env file and then run the docker-compose
```
app->.env
REDIS_IP_ADDRESS='xxx.xxx.xx.xx'
REDIS_PORT=6379
REDIS_USERNAME='xxxxx'
CACHE_EXPIRE_AFTER=2500000

docker-compose build
docker-compose up -d
```

Testing the service is provided below. Again add a .env file as below. The CACHE_SERVER_API ip address is the IP address of the machine hosting the cache
```
test_webshrinker->.env
CACHE_SERVER_API = "http://xxx.xxx.xx.xx:80/webshrinker/"
WEBSHRINKER_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXX"
WEBSHRINKER_SECRET_KEY = "YYYYYYYYYYYYYYYYYYYY"

cd test_webshrinker
python3 test_webshrinker.py https://memeburn.com/2020/07/surgeons-pose-in-bikinis-on-social-media-after-study-draws-ire/
```
