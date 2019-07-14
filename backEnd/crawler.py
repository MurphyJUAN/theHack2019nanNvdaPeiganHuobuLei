import urllib.request
from bs4 import BeautifulSoup
import json as simplejson
import re
 


def parseUrl(url):
  page = urllib.request.urlopen(url)
  page = simplejson.load(page)
  return page


def getSimilarArticle(text):
  page = parseUrl('https://www.googleapis.com/customsearch/v1?key=AIzaSyCK_LJdy-OnPgJeykI44fiEcIUItlUSNrk&cx=006431901905483214390:i3yxhoqkzo0&num=10&siteSearch=indiacelebrating.com&q=' + str(text))
  result = page['items']
  response = []
  for i in range(0,10):
    article = {}
    target = result[i]
    link = target['link']
    data = urllib.request.urlopen(link).read()
    data = data.decode('UTF-8')
    soup = BeautifulSoup(data, 'html.parser')
    article['title'] = soup.select('.entry-title')[0].text
    article['content'] = soup.select('.post-content')[0].text
    res = soup.find(class_='rating-stars')
    article['value'] = float(re.findall(r"\d+\.?\d*",res['title'])[0])
    article['url'] = link
    response.append(article)
  return(response)


