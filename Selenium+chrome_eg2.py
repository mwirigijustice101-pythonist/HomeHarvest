from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

element_list = []

#Set up chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("--headless") #Run in the headless mode(optional)
options.add_argument("--no sandbox")
options.add_argument("--disable-dev-shm-usage")

#use a proper service object
service = Service(ChromeDriverManager().install())

for page in range(1, 3):
    #Initialize driver properly
    driver = webdriver.Chrome(service=service, options=options)

    #Load the URL
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D"
    driver.get(url)
    time.sleep(2) # optional wait to ensure page loads

    #Extract product details
    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    descriptions = driver.find_elements(By.CLASS_NAME, "decription")
    ratings = driver.find_elements(By.CLASS_NAME, "ratings")

    #store results in a list
    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text,
        ])
    driver.quit()

    #Display extracted data
    for row in element_list:
        print(row)



