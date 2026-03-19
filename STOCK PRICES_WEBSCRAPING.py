import requests
import soup
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {"user-agent": "Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) \
              AppleWebkit/537.36 (KHTML, like Gecko) \
               Chrome/84.0.4147.105 Safari/537.36"}

#step2COLLECT URLs to scrap
urls = [
    "https://groww.in/us-stock/nke",
    "https://groww.in/us-stock/ko",
    "https://groww.in/us-stock/mft",
    "https://groww.in/us-stock/m-india",
    "https://groww.in/us-stock/m-axp",
    "https://groww.in/us-stock/amgn",
    "https://groww.in/us-stock/aapl",
    "https://groww.in/us-stock/ba",
    "https://groww.in/us-stock/csco",
    "https://groww.in/us-stock/gs",
    "https://groww.in/us-stock/ibm",
    "https://groww.in/us-stock/intc",
    "https://groww.in/us-stock/jpm",
    "https://groww.in/us-stock/mcd",
    "https://groww.in/us-stock/crm",
    "https://groww.in/us-stock/vz",
    "https://groww.in/us-stock/v",
    "https://groww.in/us-stock/wmt",
    "https://groww.in/us-stock/dis",
    ]

#step3:Retrieving Element Ids
class USPh14Head:
    pass


class Soup:
    pass


Company = soup.find_all("h1",{"class":"usph14Head displaySmall"}).text

Price = Soup({"class": "uht141Pri contentPrimary"
"displayBase"}).find_all("td")[1].text

change = soup.find("div",{"class":"uht141Pri contentPrimary displayBase"}).text
volume= soup.find("table",{"class":"tb10Table col l5"}).find_all("td")[1].text


