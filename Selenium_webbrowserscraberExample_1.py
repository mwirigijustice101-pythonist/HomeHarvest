from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.co.in/search?q=geeksforgeeks")
#driver = webdriver.Firefox browser using GeckoDriver.Selenium will now automate this brower window.
#Selenium automate browsers like chrome or Firefox,wait for content to load,click buttons,scroll and extract fully renderd webpages just like a real user.
#some websites load their content dynamically using javascript.This mans the data you're trying to escape may not be present in the initial HTML source.In such cases,BeautifulSoup alone won't work,because it only reads static HTML.
#WEBDRIVER=Is a software component that Selenium uses to interact with a web browser.It acts as the bridge between your python script and the actual browser window.
#Eeach browser(Chrome,Firefox,Edge,etc)has its own Webdriver:
#Chrome>chromeDriver,Firefox>GeckoDriver,Edge>EdgeDriver
#Selenium uses the WebDriver to;oPEN AND CONTROL THE BROWSER,LOAD WEBPAGES,EXTRACTELEMENTS,SIMULATE CLICKS,SCROLLS AND INPUTS



