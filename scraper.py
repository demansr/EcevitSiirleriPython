import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import bs4
import re
url = "https://www.antoloji.com/omer-hayyam/?sayfa=8"
url2 = "https://www.antoloji.com"
sayfa = requests.get(url)
corba = BeautifulSoup(sayfa.content,"html.parser")
#linkler = corba.find_all(class_="poem-title-pop")
linkler = corba.findAll("div", {"class": "poem-title-pop"})
for tags in linkler:
    myList = []
    linkler = tags.a.get("href")
    url3= url2+linkler
    page = requests.get(url3)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(class_="pd-text")
    result = result.prettify()
    result = soup.find_all("p")[2].get_text()
    file = open("yeni.txt", "a")
    result = str(result)
    file.write(result)
