import requests
from lxml import html
from bs4 import BeautifulSoup
import ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

post = "https://lpse.jakarta.go.id/eproc4/login"

data = {"txtUserId": "admin.wallezz",
        "txtPassword": "[B@29eb24fa",
        "isRekanan": "true",
	"authenticityToken": "ee6f6ef22da893b0a07f2e1f02a58fea93952110"
        }

with requests.Session() as s:
    r = s.post(post, data=data, verify=False)
    print(r.content)
    r = s.get("https://lpse.jakarta.go.id/eproc4/home")
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.title.text)
