'''
USAGE:
python3 test_webshrinker.py www.mg.co.za

Requires:
.env file with
CACHE_SERVER_API
WEBSHRINKER_ACCESS_KEY
WEBSHRINKER_SECRET_KEY
'''

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from base64 import urlsafe_b64encode
import hashlib
import requests
import json
import os
import sys
from dotenv import load_dotenv
load_dotenv()
CACHE_SERVER_API = os.getenv("CACHE_SERVER_API")
WEBSHRINKER_ACCESS_KEY = os.getenv("WEBSHRINKER_ACCESS_KEY")
WEBSHRINKER_SECRET_KEY = os.getenv("WEBSHRINKER_SECRET_KEY")


def webshrinker_categories_v3(server_api,access_key, secret_key, url=b"", params={}):
    params['key'] = access_key
    request = "categories/v3/{}?{}".format(urlsafe_b64encode(url).decode('utf-8'), urlencode(params, True))
    request_to_sign = "{}:{}".format(secret_key, request).encode('utf-8')
    signed_request = hashlib.md5(request_to_sign).hexdigest()
    return server_api + "{}&hash={}".format(request, signed_request)


access_key = WEBSHRINKER_ACCESS_KEY
secret_key = WEBSHRINKER_SECRET_KEY
url_webpage =  str(sys.argv[1])
url = url_webpage.encode('utf-8')

api_url = webshrinker_categories_v3(CACHE_SERVER_API, access_key, secret_key, url)
response = requests.get(api_url)
status_code = response.status_code
data = response.json()

if status_code == 200:
    # Do something with the JSON response
    print(json.dumps(data, indent=4, sort_keys=True))
elif status_code == 202:
    # The website is being visited and the categories will be updated shortly
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
