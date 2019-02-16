from bs4 import BeautifulSoup
import requests

r = requests.get('https://lpse.jakarta.go.id/eproc4/home')
data = r.text
soup = BeautifulSoup(data, "html.parser")

#return author name
for tabel in soup.findAll('tblStatusLelang'):
        print (tabel.get)

