from pprint import pprint
import json

with open('malData.json') as f:
    jsonData = json.load(f)

count = 0
total = 0
for i in jsonData:
    total += 1
    if  float(i['score']) >= 9.0:
        count += 1;

print (count)
