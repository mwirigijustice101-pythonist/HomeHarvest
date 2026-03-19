#import module
from gnewsclient import gnewsclient

#declare a NewsClient object
client = gnewsclient.NewsClient(language="english",location="america",topic="business",max_results=10 )

#get news feed
client.get_news()

#print location
print("Location: \n",client.locations)
print()

#print languages
print("Languages: \n",client.languages)
print()

#print topics
print("Topics \n",client.topics)
print()

news

from gnewsclient import gnewsclient
client = gnewsclient.NewsClient(language="english",
                                location="america",
                                topic="business",
                                max_results=10)
news_list = client.get_news()

for item in news_list:
    print("Title: ",item["title"])
    print("Link: ",item["link"])
    print("")





