from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.reddit.com/r/Overwatch/'
response = requests.get(url, timeout=300)
content = BeautifulSoup(response.content, "html.parser")
tweetArr = []

print(content)

# for tweet in content.find_all('div', attrs={"class": "tweetcontainer"}):
#     tweetObject = {
#         "author": tweet.find('h2', attrs={"class": "author"}).text,
#         "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
#         "tweet": tweet.find('p', attrs={"class": "content"}).text,
#         "likes": tweet.find('p', attrs={"class": "likes"}).text,
#         "shares": tweet.find('p', attrs={"class": "shares"}).text
#     }
#     tweetArr.append(tweetObject)
#
# with open('twitterData.json', 'w') as outfile:
#     json.dump(tweetArr, outfile)

# count = 0
#
# for head in content.find_all('div', attrs={"class": "_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3  "}):
#     #head.find('div', attrs={"class": "_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe "})
#     print(head.find('h3', attrs={'class': "_eYtD2XCVieq6emjKBH3m"}).text)
#
#     if count > 100:
#         break
#     count+=1
#
# print("cat")
