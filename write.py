import gzip
import json

jsonfilename='response.txt'
with gzip.GzipFile(jsonfilename, 'r') as fin:
    data = json.loads(fin.read().decode('utf-8'))