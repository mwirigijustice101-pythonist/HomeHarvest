#REQUEST MODULE:used for making HTTPrequest to a specific URL and returns the response
import requests
from bs4 import BeautifulSoup

#Fetch and parse the page
res = requests.get("https://www.geeksforgeeks.org/python-programming-language-tutorial/")
print(res.status_code)
print(res.content)
#requests.get(url):sends a GET request to the given URL
#response.status_code:Returns HTTP status code(200 = success).not
#response.content:Returns the raw HTML of the page in bytes.

soup = BeautifulSoup(res.content, "html.parser")
print(soup.prettify())
#BeautifulSOUP(html,parser):Converts HTML into searchable object."html.parser" is the built-in parser.
#soup.prettify():Formats tha Html nicely for easier reading.

#Find the main content container
content = soup.find("div", class_="article--viewer_content")
if content:
    for para in content.find_all("p"):
        print(para.text.strip())
else:
    print("No article content found.")

