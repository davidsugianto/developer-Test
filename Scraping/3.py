import requests
from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://lpse.jakarta.go.id/eproc4/login", verify=False)
form = br.get_form()
form['txtUserId'] = "admin.wallezz"
form['txtPassword'] = "[B@29eb24fa"
form['isRekanan'] = "true"
br.submit_form(form)

src = str(br.parsed())

print(src.title.text)

