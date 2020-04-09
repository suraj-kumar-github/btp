#this is not working currently
#run this file in jupyter part by part

import requests
from bs4 import BeautifulSoup

url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')

news_items = []

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['image'] = item.content['url']
    news_items.append(news_item)

print(news_items)