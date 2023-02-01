import requests
from b4 import BeautifulSoup
def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
  url=input("Enter url to crawl");
  #url = 'https://lyricfind.ga/page=' + str(page)
  source_code = requests.get(url)
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text)
  for link in soup.findAll('a', {'class': 'Name'}):
  href = "https://lyricfind.ga" + link.get('href')
  title = link.string
   print(href)a
  print(title)
  get_single_item_data(href)
  page += 1
def get_single_item_data(item_url):
  source_code = requests.get(item_url)
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text)
  for item_name in soup.findAll('div', {'class': 'i-name'}):
  print(item_name.string)
  for link in soup.findAll('a'):
  href = "https://lyricfind.ga" + link.get('href')
  print(href)
trade_spider(3)
