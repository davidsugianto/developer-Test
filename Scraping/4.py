from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='/usr/local/share/chromedriver', chrome_options=option)

browser.get("https://lpse.jakarta.go.id/eproc4/home", verify=False)

timeout = 20

titles_element = browser.find_elements_by_xpath("//a[@class='[ADMIN.WALLEZZ] - 81.562.803.7-027.000']")

titles = [x.text for x in titles_element]

print('TITLES:')
print(titles, '\n')

table_element = browser.find_elements_by_xpath("//p[@class='tblStatusLelang']")
table = [x.text for x in language_element]

print("Data Table:")
print(table, '\n')

for title, language in zip(titles, table):
    print("Data : Tabel")
    print(title + ": " + table, '\n')
