'''
This gets free ips

#######################################################
Use Elite Proxies whenever possible if you are using Free Proxies ( or even if you are paying for proxies )
All proxies aren’t the same. There are mainly three types of proxies available in the internet.

Transparent Proxy – A transparent proxy is a server that sits between your computer and the internet and redirects your requests and responses without modifying them. It sends your real IP address in the HTTP_X_FORWARDED_FOR header, this means a website that does not only determine your REMOTE_ADDR but also checks for specific proxy headers that will still know your real IP address. The HTTP_VIA header is also sent, revealing that you are using a proxy server.

Anonymous Proxy – An anonymous proxy does not send your real IP address in the HTTP_X_FORWARDED_FOR header, instead, it submits the IP address of the proxy or it’ll just be blank. The HTTP_VIA header is sent with a transparent proxy, which would reveal you are using a proxy server. An anonymous proxy server does not tell websites your real IP address anymore. This can be helpful to just keep your privacy on the internet. The website can still see you are using a proxy server, but in the end, it does not really matter as long as the proxy server does not disclose your real IP address. If someone really wants to restrict page access, an anonymous proxy server will be detected and blocked.

Elite Proxy – An elite proxy only sends REMOTE_ADDR header while the other headers are empty. It will make you seem like a regular internet user who is not using a proxy at all. An elite proxy server is ideal to pass any restrictions on the internet and to protect your privacy to the fullest extent. You will seem like a regular internet user who lives in the country that your proxy server is running in.

Elite Proxies are your best option as they are hard to be detected. Use anonymous proxies if it’s just to keep your privacy on the internet. Lastly, use transparent proxies – although the chances of success are very low.
#######################################################
'''
import re
from itertools import cycle

import requests
from bs4 import BeautifulSoup


def get_https_ips():
    # get html page and load it with Beautiful Soup
    r = requests.get('https://free-proxy-list.net/')
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    # find the ip addresses
    table = soup.find('table', id='proxylisttable')
    trs = table.find_all('tr')

    # yield ip addresses that support https
    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) is 8:
            (ip, port, code, country, anonymity, google, https, last_checked) = tds
            if https.get_text() == 'yes':
                yield ":".join([ip.get_text(), port.get_text()])

proxies = list(get_https_ips())
proxy_pool = cycle(proxies)

for i in range(1, 100):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d" % i)
    try:
        print(f'proxy: {proxy}')
        response = requests.get('https://httpbin.org/ip', proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
        print("Skipping. Connnection error")
    print()
