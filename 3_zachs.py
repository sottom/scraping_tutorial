# imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# open zacks
options = Options()
options.headless = True
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.zacks.com/stock/research/AAPL/earnings-announcements')

# get data
obj_data = browser.execute_script('return window.document.obj_data')
browser.close()
