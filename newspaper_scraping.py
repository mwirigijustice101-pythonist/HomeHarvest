import newspaper
import feedparser

def scrape_new_from_feed(feed_url):
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        # Create a newspaper article object
        article = newspaper.Article(entry.link)
        # download and parse the article
        article.download()
        article.parse()
        # extract relevant information
        article.append({
            "title" : article.title,
            "author" : article.authors,
            "publish_date" : article.publish_date,
            "content" : article.text
        })
    return articles

feed_url = "https://feeds.bbci.co.uk/news/rss.xml"
articles = scrape_new_from_feed(feed_url)

#print the extracted articles
for article in articles:
    print("Title: " + article["title"])
    print("Author: " + article["author"])
    print("Publish Date: " + article["publish_date"])
    print("Content: " + article["content"])
    print()




