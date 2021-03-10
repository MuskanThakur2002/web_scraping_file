from saraltask4and5 import scrape_movie_details
from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
name=BeautifulSoup(data.text, "html.parser")
def analyse_movies_language(soup):
    language_movie=[]
    unique_language=[]
    for lan in soup:
        language_movie.append(lan["movie_language"])
    print(language_movie)
    for i in language_movie:
            for k in i:
                if k not in unique_language:
                    unique_language.append(k)
    print(unique_language)
    new_dict={}
    for i in unique_language:
        count=1
        for j in language_movie:
            for k in j:
                if i == k:
                    count=count+1
        new_dict[i]=count
    data=open("saraltask6.json","w")
    saral=json.dumps(new_dict, indent=4)
    data.write(saral)
    print(new_dict)
analyse_movies_language(scrape_movie_details(movie_function(name)))