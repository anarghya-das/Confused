import http.client, urllib.request, urllib.parse, urllib.error, base64
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

headers = {
    # Request headers
    'Subscription-Key': '3a5f419cd2b04164933ee603e990b8ff',
}

params = urllib.parse.urlencode({
})

conn = http.client.HTTPSConnection('api.wegmans.io')
conn.request("GET", "/products/11914?api-version=2018-10-18&%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
parsed=json.loads(data)
print(json.dumps(parsed, indent=4))
conn.close()
