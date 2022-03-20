import requests
from bs4 import BeautifulSoup
from declarations import IsimlerErkek, Base


def Start():
    for i in range(84):
        page = str(i+1)
        htsml = requests.get("https://turkadlar.com/?s=tum-adlar&sh2="+page)
        soup = BeautifulSoup(htsml.text, 'html.parser')
        table = soup.find("table", class_="ecins")
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        for r in rows:
            tds = r.find_all('td')
            kayit = IsimlerErkek(Sira=int(
                tds[0].text), Aciklama=tds[1].text, KullanimSayi=tds[2].text.replace('kişi', '').strip())
            kayit.Add()
