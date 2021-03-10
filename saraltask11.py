from saraltask4and5 import scrape_movie_details
from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
name=BeautifulSoup(data.text, "html.parser")

def director_analysis(soup):
    genres_movie=[]
    unique_genres=[]
    for lan in soup:
        genres_movie.append(lan["genres"])
    # print(genres_movie)
    for i in genres_movie:
        if i not in unique_genres:
            # for k in i:
            if i not in unique_genres:
                unique_genres.append(i)
    # print(unique_genres)
    new_dict={}
    for i in unique_genres:
        count=1
        for j in genres_movie:
            # for k in j:
            if i == j:
                count=count+1
        new_dict[i]=count
    data=open("saraltask11.json","w")
    saral=json.dumps(new_dict, indent=4)
    data.write(saral)
    pprint(new_dict)
director_analysis(scrape_movie_details(movie_function(name)))