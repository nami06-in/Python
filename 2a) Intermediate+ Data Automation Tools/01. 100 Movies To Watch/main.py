import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

web_page_contents = response.text
soup = BeautifulSoup(web_page_contents, "html.parser")

list_of_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
titles = list_of_titles[::-1]
print(titles)

with open("movies.txt", "a", encoding="utf-8") as file:
    for title in titles:
        file.write(title + "\n")
