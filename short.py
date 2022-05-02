import urllib
import json
from pprint import pprint
import time
import requests
key = 'aff31d261c1dac351fe3c354f233d06d706c1'
link = input('Enter the link you want to short : ')
time.sleep(0.5)
print("Checking Your URL...")
lurl = urllib.parse.quote(link)
r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, lurl))
check = (r.json()['url']['status'])
time.sleep(1)
if check!=7:
  print("Invalid URL! Try again.")
  exit()
date = (r.json()['url']['date'])
title = (r.json()['url']['title'])
finalLink = (r.json()['url']['shortLink'])
print("Successfully Shortened The URL!")
time.sleep(1)
print("Date :",date)
print("Title :",title)
print("Short Link :",finalLink)
