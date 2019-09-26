from pprint import pprint
import json

with open('twitterData.json') as f:
    jsonData = json.load(f)

count = 0

for i in jsonData:
    if "obama" in i['tweet'].lower():
        count += 1;

print (count)
