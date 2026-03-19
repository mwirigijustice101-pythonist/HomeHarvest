from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.parse

website = "https://www.trulia.com/NY/New York"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.o; Win64; x64;)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
response = requests.get(website, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

result = soup.find_all("li", {"class" :
                               "Grid__CellBox-sc-144isrp-0"
                               "SearchResultsList__WideCell-b7y9ki-2 jiZmPM"})

result_update = soup.find_all("div", class_="website = ‘https://www.trulia.com/NY/New_York/'= ‘https://www.trulia.com/NY/New_York/'")

address = [result.find("div", {"data-testid":"property-address"}).get_text() for result in result_update]
beds = [result.find("div", {"data-testid":"property-beds"}).get_text() for result in result_update]
baths = [result.find("div",{"data-testid":"property-baths"}).get_text() for result in result_update]
prices = [result.find("div", {"data-testid":"property-price"}).get_text() for result in result_update]
