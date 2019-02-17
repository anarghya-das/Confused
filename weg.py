import http.client, urllib.request, urllib.parse, urllib.error, base64
import gzip
import json

headers = {
    # Request headers
    'Subscription-Key': '3a5f419cd2b04164933ee603e990b8ff',
}

params = urllib.parse.urlencode({
})

conn = http.client.HTTPSConnection('api.wegmans.io')
conn.request("GET", "/meals/recipes/21472?api-version=2018-10-18&%s" % params, "{body}", headers)
response = conn.getresponse()
data=response.read()
print(data)