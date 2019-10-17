# coding: utf-8
#######################################################
# THIS CODE DOES NOT WORK ON PURPOSE (DEMONSTRATION)
#######################################################
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Send GET request to page
response = requests.get('https://www.timeanddate.com/holidays/us/')

# Grab the innerHTML and load into Beautiful Soup
soup = BeautifulSoup(response.text, 'lxml')

# make sure table exists
rows = soup.find('table', id='holidays-table').find_all('tr', class_='showrow')
print(rows)
