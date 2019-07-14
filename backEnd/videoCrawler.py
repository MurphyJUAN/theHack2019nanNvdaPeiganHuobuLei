import urllib.request
from bs4 import BeautifulSoup
import json as simplejson
import re
 


def parseUrl(url):
  page = urllib.request.urlopen(url)
  page = simplejson.load(page)
  return page


def getSimilarVideo(text):
  url = "https://www.googleapis.com/youtube/v3/search?id=7lCDEYXw3mM&key=AIzaSyC7go5QGCtQPEJypFNd3MmXTypSpSCmcvU&part=snippet&type=video&videoCaption=closedCaption&q=" + str(text)
  page = parseUrl(url)
  # print(page)
  result = page['items']
  for i in range(0,1):
    article = {}
    target = result[i]
    vid = target['id']
    target = vid['videoId']
return target