import requests
from bs4 import BeautifulSoup
from declarations import IsimlerKadin, Base


def Start():
    for i in range(82):
        page = str(i+1)
        htsml = requests.get("https://turkadlar.com/?s=tum-adlar&sh="+page)
        soup = BeautifulSoup(htsml.text, 'html.parser')
        table = soup.find("table", class_="kcins")
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        for r in rows:
            tds = r.find_all('td')
            kayit = IsimlerKadin(Sira=int(
                tds[0].text), Aciklama=tds[1].text, KullanimSayi=tds[2].text.replace('kişi', '').strip())
            kayit.Add()
