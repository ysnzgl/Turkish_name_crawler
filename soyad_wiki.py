from urllib import request
from bs4 import BeautifulSoup
import requests


def soyadci(text):
    text =requests.get(text)
    soup=BeautifulSoup(text.text)
    div= soup.find("div",class_="mw-category-columns")
    lis=div.find_all("li")
    for li in lis:
        print(li.text)


soyadci("https://tr.wikipedia.org/w/index.php?title=Kategori:T%C3%BCrk%C3%A7e_soyadlar%C4%B1")
soyadci("https://tr.wikipedia.org/w/index.php?title=Kategori:T%C3%BCrk%C3%A7e_soyadlar%C4%B1&pagefrom=%C3%87olak#mw-pages")
soyadci("https://tr.wikipedia.org/w/index.php?title=Kategori:T%C3%BCrk%C3%A7e_soyadlar%C4%B1&pagefrom=K%C4%B1l%C4%B1%C3%A7lar#mw-pages")
soyadci("https://tr.wikipedia.org/w/index.php?title=Kategori:T%C3%BCrk%C3%A7e_soyadlar%C4%B1&pagefrom=Sezek#mw-pages")
