import random
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# URl to web scrap from.
page_url = 'https://www.cyberpuerta.mx/Computadoras/Webcam-Audio/Webcams/'

# Rotating User Agents
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (XHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (XHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

# Pick a random user agent
user_agent = random.choice(user_agent_list)

# Set the headers
headers = {'User-Agent': user_agent}

# Make the request
response = Request(page_url, headers=headers)

# opens the connection and downloads html page from url
uClient = urlopen(response)

# parses html into a soup data structure to traverse html
page_soup = BeautifulSoup(uClient.read(), "html.parser")
uClient.close()

print(page_soup.p)
#hola
#HEY
#Cambio2