import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)

soup = BeautifulSoup(response.text, "lxml")
title = soup.find_all(name='h3', class_="title")

movie_titles = [movie.get_text() for movie in title]
movies=movie_titles[::-1]

with open ('movies.txt','w',encoding='utf-8') as f:
    for indent in movies:
        f.write(f'{indent}\n')
