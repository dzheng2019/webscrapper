from bs4 import BeautifulSoup
import requests
import json

url = 'https://myanimelist.net/topanime.php?limit='
response = requests.get(url, timeout=300)
content = BeautifulSoup(response.content, "html.parser")
listArr = []

for x in range(100):
    url = 'https://myanimelist.net/topanime.php?limit=' + str((x*50))
    response = requests.get(url, timeout=300)
    content = BeautifulSoup(response.content, "html.parser")

    for listing in content.find_all('tr', attrs={"class": "ranking-list"}):
        listObject = {
            "name": listing.find('a', attrs={"class": "hoverinfo_trigger fl-l fs14 fw-b"}).text,
            "score": listing.find('span', attrs={"class": "text on"}).text
        }
        listArr.append(listObject)

with open('malData.json', 'w') as outfile:
    json.dump(listArr, outfile)
