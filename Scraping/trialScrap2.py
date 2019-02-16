import requests
from lxml import html
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


USERNAME = "admin.wallezz"
PASSWORD = "[B@29eb24fa"
REKANAN  = "true"
TOKEN	 = "ee6f6ef22da893b0a07f2e1f02a58fea93952110"

LOGIN_URL = "https://lpse.jakarta.go.id/eproc4/login"
URL = "https://lpse.jakarta.go.id/eproc4/home"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL, verify=False)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticityToken']/@value")))[0]

    # Create payload
    payload = {
        "txtUserId": USERNAME,
        "txtPassword": PASSWORD,
	"isRekanan": REKANAN,
        "authenticityToken": TOKEN
    }

    # Perform login
    #result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    result = requests.get(LOGIN_URL, auth=(USERNAME,PASSWORD))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='tblStatusLelang']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
