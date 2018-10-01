#!/usr/bin/env python3
import pyperclip
import requests
try: 
        from BeautifulSoup import BeautifulSoup
except ImportError:
        from bs4 import BeautifulSoup

## Get text from clipboard
text=pyperclip.paste()

## base URL
url = 'http://www.morfix.co.il/'

## read URL
def getHtml():
    try:
        r = requests.get(url+text) 
    except IndexError:
        r = 1
    return r

## extension title
print("PyMilon\n--")

## extension output
if len(text.split(' ')) > 3:
    print("No term specified")
else:
    r = getHtml()
    if r == 1:
        print("No term specified")
    else:
        try:
            html = r.content
            parsed_html = BeautifulSoup(html, "lxml")
            result = parsed_html.body.find('div', attrs={'class':'default_trans'}).text
            print(result)
        except AttributeError:
            try:
                result = parsed_html.body.find('div', attrs={'class':'translation translation_he heTrans'}).text 
                print(result)
            except AttributeError:
                print("No term specified")


