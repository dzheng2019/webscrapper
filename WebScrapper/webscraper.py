from bs4 import BeautifulSoup
import requests
import json
import math
from math import *
# tutorial-env\Scripts\activate.bat

url = 'https://myanimelist.net/topanime.php?limit='
response = requests.get(url, timeout=3000)
content = BeautifulSoup(response.content, "html.parser")
listArr = []

count=1
for y in range(0,100,2):
    listArr = []
    for x in range(y,y+2):
        #print("lightLink top-anime-rank-text rank" + str(1+ math.floor(math.log10(count))))
        url = 'https://myanimelist.net/topanime.php?limit=' + str((x*50))
        print(url)
        response = requests.get(url, timeout=3000)
        content = BeautifulSoup(response.content, "html.parser")
        for listing in content.find_all('tr', attrs={"class": "ranking-list"}):
            listObject = {
                "num": count,
                "name": listing.find('a', attrs={"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text,
                "score": listing.find('span', attrs={"class": "text on"}).text
            #    "rank": listing.find('span', attrs={"class": "lightLink top-anime-rank-text rank" + str(1+ math.floor(math.log10(count)))}).text
            }
            listArr.append(listObject)
            count+=1
    with open('datafiles/malData' + str(y) + '.json', 'w') as outfile:
        json.dump(listArr, outfile)
