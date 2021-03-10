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
    director_movie=[]
    unique_director=[]
    for lan in soup:
        director_movie.append(lan["director"])
    print(director_movie)
    for i in director_movie:
        if i not in unique_director:
            for k in i:
                if k not in unique_director:
                    unique_director.append(k)
    print(unique_director)
    new_dict={}
    for i in unique_director:
        count=1
        for j in director_movie:
            for k in j:
                if i == k:
                    count=count+1
        new_dict[i]=count
    data=open("saraltask7.json","w")
    saral=json.dumps(new_dict, indent=4)
    data.write(saral)
    print(new_dict)
director_analysis(scrape_movie_details(movie_function(name)))