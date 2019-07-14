# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
import json
import requests


KEYWORDS_URL = 'http://api.bosonnlp.com/keywords/analysis'


text = '病毒式媒体网站：让新闻迅速蔓延'
params = {'top_k': 10}
data = json.dumps(text)
headers = {
    'X-Token': 'YOUR_API_TOKEN',
    'Content-Type': 'application/json'
}
resp = requests.post(KEYWORDS_URL, headers=headers, params=params, data=data.encode('utf-8'))


print(resp.json())
for word in resp.json():
    print(word)