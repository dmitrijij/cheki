import encodings
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import encodings
import time


def get_data(link):
    listing=[]

    headers = {"User-Agent": UserAgent().random}

    full_page = requests.get(link, headers=headers)
    soup = BeautifulSoup(full_page.content, "html.parser")

    sell = soup.findAll("div", {"class": "aJThHsRzJ hsLgGFlow bJThHsRzJ tJThHsRzJ BJThHsRzJ"})
    sell = sell[0].text
    listing.append(to_float(sell))

    try:
        estimation = soup.findAll("div", {"class": "aJThHsRzJ bSbeMcXxl bJThHsRzJ tJThHsRzJ"})
        estimation = estimation[0].text
    except:
        estimation = "0,0"
    listing.append(to_float(estimation))
    name = soup.findAll("h1", {"class": "a3La7AH14 b3La7AH14"})
    listing.append((name[0]).text)


    return listing


def to_float(n):
    n = n.split()[0]
    n = n.split(",")
    n = float(".".join(n))

    return n


f=open("input.txt","r")
listmar=[]
listmar=f.read().split()
print(listmar)
f.close()
c=0
fo=open("output.txt","w",encoding="utf-8")
fo.write("[")

for i in listmar:
    c+=1
    fo.write(str(get_data(i)))
    if c!= len(listmar):
        fo.write(",")
fo.write("]")
fo.close()


