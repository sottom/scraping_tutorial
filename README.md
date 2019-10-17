# Web Scraping
- [Web Scraping](#web-scraping)
  - [Getting Started](#getting-started)
  - [Websites for Scraping Tutorial (Tech Talk):](#websites-for-scraping-tutorial-tech-talk)
  - [Important Points](#important-points)
    - [Be Respectful](#be-respectful)
    - [Can websites figure out you're scraping them?](#can-websites-figure-out-youre-scraping-them)
    - [How do I make my scraper more humanlike?](#how-do-i-make-my-scraper-more-humanlike)
    - [When you run into issues, start Googling](#when-you-run-into-issues-start-googling)
  - [Why Scrape?](#why-scrape)
  - [What to do before scraping](#what-to-do-before-scraping)
  - [Requests & BeautifulSoup](#requests--beautifulsoup)
    - [When to use it](#when-to-use-it)
    - [Example usage](#example-usage)
    - [Notes](#notes)
  - [Headless Browser](#headless-browser)
    - [When to use it](#when-to-use-it-1)
    - [Example usage](#example-usage-1)
    - [Notes](#notes-1)
  - [Chrome Extension](#chrome-extension)
    - [When to use it](#when-to-use-it-2)
    - [Notes](#notes-2)
  - [Scraping Framework like Scrapy](#scraping-framework-like-scrapy)
    - [When to use it](#when-to-use-it-3)


## Getting Started
```python
git clone https://github.com/sottom/scraping_tutorial.git
pip install -r requirements.txt
python {any_file}.py
```

## Websites for Scraping Tutorial (Tech Talk):

1. https://www.ratemyprofessors.com/
2. https://www.premierleague.com/players
3. https://www.zacks.com/stock/research/AAPL/earnings-announcements
4. https://free-proxy-list.net/
5. https://www.timeanddate.com/holidays/us/
6. https://codepen.io/gaearon/pen/oWWQNa


## Important Points
### Be Respectful
- Look at and follow the /robots.txt file
- Don't make too many requests
- don't publish data that isn't yours (be careful about this)
### Can websites figure out you're scraping them?
- Yes.
### How do I make my scraper more humanlike?
- Change User-Agents
- Change IP addresses
- Don't follow the same pattern every time you scrape
    - Scraping Intervals
    - Scraping Click Paths
    - Click Timing
    - Click position is hard, because a click has no `screenX` or `screenY`
### When you run into issues, start Googling
- [Great overview of web scraping](https://pluralsight.com/guides/advanced-web-scraping-tactics-python-playbook)
- [How to prevent getting blacklisted](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)
- [Most common User-Agents](https://techblog.willshouse.com/2012/01/03/most-common-user-agents/)
- [Solving Captchas](https://www.scrapehero.com/how-to-solve-simple-captchas-using-python-tesseract/)



## Why Scrape?
- Really come to understand how the web works
- get data not available from APIs
- interview prep


## What to do before scraping
- check for APIs
    - 1_professor.py
    - 2_sports.py
- check for data in the global scope
    - 3_zachs.py


## Requests & BeautifulSoup
### When to use it
- when the data you want is loaded on page startup
### Example usage
- 4_proxy.py
- 5_holidays.py
### Notes
- could use regex, could use other parsers, doesn't matter


## Headless Browser
### When to use it
- when code is rendered by javascript, otherwise you don't get what you expect ([React App](https://codepen.io/gaearon/pen/oWWQNa))
- when you need to login
- use for web automation
### Example usage
- 6_holidays2.py
- learningsuite (not included)
### Notes


## Chrome Extension
### When to use it
- when selenium doesn't work
### Notes
- chrome extensions do a ton more than scrape
- out of scope


## Scraping Framework like Scrapy
### When to use it
- When you want to run a big operation and scrape on multiple threads (for complex projects)
- [comparison site](https://towardsdatascience.com/scrapy-vs-selenium-vs-beautiful-soup-for-web-scraping-24008b6c87b8)
