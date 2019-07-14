# -*- coding: utf-8 -*- 
from aylienapiclient import textapi
import crawler
import json


def analyzeValue(para):
    
    c = textapi.Client("3f0bd976", "6b6565eed1a5d6bdaddee4823903727f")
    
    s = c.Sentiment({'text': para})    
    #classify = c.ClassifyByTaxonomy({'text': "Jim is a singer and jumper", 'taxonomy': "iab-qag"})
    
    #summary = c.Summarize('http://techcrunch.com/2014/02/27/aylien-launches-text-analysis-api-to-help-developers-extract-meaning-from-documents/')
    #print(summary)
    #print(classify)
    
    value = 0
    
    if s['polarity'] == 'positive':
        value += s['polarity_confidence']
    else:
        value -= s['polarity_confidence']
    
    if s['subjectivity'] == 'objective':
        value += s['subjectivity_confidence']
    else:
        value -= s['subjectivity_confidence']    
    
    #print(value, s)
    return value

def defineType(para):
    
    c = textapi.Client("3f0bd976", "6b6565eed1a5d6bdaddee4823903727f")
      
    classify = c.ClassifyByTaxonomy({'text': para, 'taxonomy': "iab-qag"})
    

    return classify['categories'][0]['label']


def analyze(text):
    
    text_type = defineType(text).split()
    para_output = crawler.getSimilarArticle(text_type[0]) 
    largest = -2
    ret = []
    value = {'chose_para':'', 'chose_url':''}
    
    for para in para_output:
        para_value = analyzeValue(para['content'])
        if para_value > largest:
            largest = para_value
            value['chose_para'] = para['content']
            value['chose_url'] = para['url']
            
    ret.append(value)
    return json.dumps(ret)



    



    