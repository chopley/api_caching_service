from typing import Optional
from fastapi import FastAPI
import requests_cache
import os
from dotenv import load_dotenv
load_dotenv()

REDIS_IP_ADDRESS = os.getenv("REDIS_IP_ADDRESS")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
CACHE_EXPIRE_AFTER = int(os.getenv("CACHE_EXPIRE_AFTER"))


def get_webshrinker(url_request,key,hash):
    '''

    '''
    try:
        from urllib import urlencode
    except ImportError:
        from urllib.parse import urlencode

    from base64 import urlsafe_b64encode
    import hashlib
    import requests
    import requests_cache
    import json

    url_request = "https://api.webshrinker.com/categories/v3/" + url_request + "?key=" + key + "&hash=" + hash  
    response = s.get(url_request)

    status_code = response.status_code
    data = response.json()

    if status_code == 200:
        # Do something with the JSON response
        print(json.dumps(data, indent=4, sort_keys=True))
    elif status_code == 202:
        # The website is being visited and the categories will be updated shortly
        s.cache.delete_url(url_request)
        print(json.dumps(data, indent=4, sort_keys=True))
    elif status_code == 400:
        # Bad or malformed HTTP request
        print("Bad or malformed HTTP request")
        print(json.dumps(data, indent=4, sort_keys=True))
    elif status_code == 401:
        # Unauthorized
        print("Unauthorized - check your access and secret key permissions")
        print(json.dumps(data, indent=4, sort_keys=True))
    elif status_code == 402:
        # Request limit reached
        print("Account request limit reached")
        print(json.dumps(data, indent=4, sort_keys=True))
    else:
        # General error occurred
        print("A general error occurred, try the request again")
    return(data)

app = FastAPI()
import redis
from requests_cache import CachedSession

r = redis.StrictRedis(host=REDIS_IP_ADDRESS,
        port=REDIS_PORT,
        password=REDIS_USERNAME)

s = CachedSession('webshrinker_cache', backend='redis', expire_after=CACHE_EXPIRE_AFTER, connection = r )

@app.get("/webshrinker/categories/v3/{url_request}")
def read_item(url_request: str, key: str, hash: str):
    from fastapi.responses import JSONResponse
    data = get_webshrinker(url_request,key,hash)
    return JSONResponse(content=data)

