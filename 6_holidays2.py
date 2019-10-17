# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# create a headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)

# navigate to page
browser.get('https://www.timeanddate.com/holidays/us/')

# Grab the innerHTML and load into Beautiful Soup
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
soup = BeautifulSoup(innerHTML, 'lxml')
browser.close()

rows = soup.find('table', id='holidays-table').find_all('tr', class_='showrow')
print(rows)
