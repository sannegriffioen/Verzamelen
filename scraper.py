from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://www.amazon.nl/")
cookie = driver.find_element(
    by=By.ID, value="sp-cc-accept")
cookie.click()
zoekbalk = driver.find_element(by=By.ID, value="twotabsearchtextbox")
zoekbalk.clear()
zoekbalk.send_keys("laptop")
zoekbalk.submit()
filters = driver.find_element(
    by=By.LINK_TEXT, value="15 tot 16 in (38 tot 41 cm)").click()
texten = []
prijzen = []

for i in range(2, 4):
    pagina = driver.find_element(by=By.TAG_NAME, value="body")
    body = pagina.get_attribute('innerHTML')
    soup = BeautifulSoup(body, 'html.parser')
    text = soup.find_all(
        'span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
    prijs = soup.find_all(
        'span', {'class': 'a-offscreen'})
    texten.append(text)
    prijzen.append(prijs)
    button = driver.find_element(
        by=By.LINK_TEXT, value=str(i)).click()
for items in texten:
    for item in items:
        print(item.get_text())
for items in prijzen:
    for item in items:
        print(item.get_text())

driver.quit()
