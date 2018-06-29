from bs4 import BeautifulSoup
from readTestData import gHtml
import requests
import time
import logging

class ResponseError(Exception):
    pass

#gHtml
# Or!
#r = requests.get('https://www.theguardian.com/world/1992/jul/24/colombia.fromthearchive')
#reqHtml = r.text

# Both refer to the same article

def extractSentences(html,bodyTag="articleBody"):
    bSp = BeautifulSoup(html,"html.parser")
    body = bSp.find(itemprop=bodyTag)

    if body is None:
        raise ResponseError('Bad tag / no sentences')
    else:
        sentences = body.text.strip().split('\n')
        sentences = [sent for sent in sentences if sent != '' and len(sent.split()) > 4]
    return(sentences)

def getSentences(url):
    time.sleep(0.5)
    print('Retrieving sentences from %s'%(url))
    try:
        r = requests.get(url)
    except ConnectionError:
        print('ConnectionError!')
        #TODO some more error handling (bad response)
    else:
        rHtml = r.text

        try:
            sentences = extractSentences(rHtml)
        except ResponseError:
            print('No sentences @ %s'%(url))
            sentences = []

    return(sentences)

url = 'https://www.theguardian.com/world/1992/jul/24/colombia.fromthearchive'

# This returns all paragraphs from the article.
# But not the byline!
