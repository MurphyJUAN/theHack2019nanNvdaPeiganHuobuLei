import urllib

import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    soup_html = BeautifulSoup(requests.get(url=url, headers=headers).content, "lxml")
    return soup_html

# Wikipedia
def get_wikipedia(message):
    url = 'https://www.britannica.com/biography/Albert-Einstein'
    soup_html = get_html(url)

    title = soup_html.find('h1').get_text().strip()
    topic = soup_html.find(class_='topic-identifier').get_text().strip()
    return title + ' is a ' + topic

# Britannica
def get_britannica(message):
    url = 'https://www.britannica.com/biography/Albert-Einstein'
    soup_html = get_html(url)

    title = soup_html.find('h1').get_text().strip()
    topic = soup_html.find(class_='topic-identifier').get_text().strip()
    return title + ' is a ' + topic


# Get a joke 
def get_joke():
    url = 'https://bestlifeonline.com/text-jokes/'    
    soup_html = get_html(url)

    contents = soup_html.select('.content')
    from random import choice
    content = choice(contents)
    result = content.get_text().strip()
    return result


if __name__ == '__main__':
    print (news())
