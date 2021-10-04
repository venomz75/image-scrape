# TODO: setup new download stream to support https

#!/usr/bin/python3
from bs4 import BeautifulSoup   #apt-get install python3-bs4
from requests_html import HTMLSession
import requests                 #pip install requests
from collections import OrderedDict
import ssl
import threading
import urllib
import urllib3
import json
import os
import re


#Constants
target_url = input("Enter target URL: ")
regex_pattern = ".*\.(jpg|png|gif)$"

session = HTMLSession()
response = session.request("GET",target_url,allow_redirects=False)
response.html.render()

soup = BeautifulSoup(response.html.html, "html.parser")
print(soup)
results = []

#Find 'img' tags
img_tags = soup.find_all("img")
img_src = [img["src"] for img in img_tags]

for url in img_src:
    results.append(url)

#Find 'a' tags with an image path in 'href'
a_tags = soup.find_all("a", attrs={"href": re.compile(regex_pattern)})
print(a_tags)
a_hrefs = [a["href"] for a in a_tags]

for href in a_hrefs:
    image = re.search(regex_pattern, href)
    if image and not href in a_results:
        results.append(href)

print("Found " + str(len(results)) + " image(s) on webpage " + target_url + ".")
context = ssl.create_default_context()

#Trim characters at start/end
for i in results:
    while i[0] == "/":
        i = i[1:]
    print(i)
    if "?" in i:
        i = i[:i.rindex("?")]
        print (i)
    
    #Attempt download
    try:
        print(i)
        urllib.request.urlretrieve(i, os.getcwd() + i[i.rindex("/"):])
        
    except:
        try:
            urllib.request.urlretrieve("http://" + i, os.getcwd() + i[i.rindex("/"):])  
        except:
            try:
                urllib.request.urlretrieve(target_url + "/" + i, os.getcwd() + i[i.rindex("/"):])
            except:
                print("Download failed, aborting.")