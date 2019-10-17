# imports
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# start a browser
options = Options()
options.headless = True
browser = webdriver.Chrome(chrome_options=options)

# navigate to the quotes page and find all quotes
browser.get('https://www.keepinspiring.me/funny-quotes/')
quotes = browser.find_elements_by_class_name('author-quotes')

# get random quote
quote = random.choice(quotes).text

# close browser
browser.close()

print(quote)
