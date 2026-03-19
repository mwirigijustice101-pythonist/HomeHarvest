import requests
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')

print(page.status_code)
print(page.content)
#requests.get():sends an HTTP GET request to the website.
#page.status_code:returns 200 if the page loaded successfully.
#page.content:returns the full HTML of the page.

from bs4 import BeautifulSoup
import requests

page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())






