import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

#access the HTML content from the IMDb top 250 movies page
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

#extract movie details using HTMLtags li tag represents a movie block containing title,year and rating details
movies = soup.select("li.ipc-metadata-summary-item")

#crate a list to store movie data
movie_data = []

for movie in movies:
    title = movie.select_one("h3.ipc-title_text").text.strip()
    year = movie.selesct_one("span.ipc-title-metadata-item").text.strip()
    rating_tag = movie.select_one("span.ipc-rating-star--rating")
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    movie_data.APPEND({
        "Title": title,
        "Year":year,
        "Rating": rating
    })

#display the extracted data
for movie in movie_data:
    print(f"{movie["Title"]} ({movie["Year"]}) - Rating: {movie['Rating']}")

#save the data into csv file
df = pd.DataFrame(movie_data)
df.to_csv("imbd_top_250_movies.csv", index=False)
print("IMDb data saved successfully to imdb_top_250_movies.csv")


