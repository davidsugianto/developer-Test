import requests
from bs4 import BeautifulSoup
import ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

username = 'admin.wallezz'
password = '[B@29eb24fa'
rekanan  = 'true'
scrape_url = 'https://lpse.jakarta.go.id/eproc4/home'

login_url = 'https://lpse.jakarta.go.id/eproc4/login'
login_info = {'txtUserId': username,'txtPassword': password,'isRekanan': rekanan}

session = requests.session()

s = session.post(url=login_url, data=login_info, verify=False)
print(s.content)

url = session.get(url=scrape_url)

soup = BeautifulSoup(url.content, 'html.parser')

print(soup.title.text)
#for tabel in soup.findAll('tblStatusLelang'):
#   print (tabel.get)

#for link in soup.findAll('a'):
#    print('\nLink href: ' + link['href'])
#    print('Link text: ' + link.text)
