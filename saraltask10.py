from saraltask4and5 import scrape_movie_details
from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
name=BeautifulSoup(data.text, "html.parser")
def analyse_language_and_directors(soup):
    director_movie=[]
    unique_director=[]
    language_movie=[]
    unique_language=[]
    for lan in soup:
        director_movie.append(lan["director"])
        language_movie.append(lan["movie_language"])
    for i in language_movie:
        for k in i:
            if k not in unique_language:
                unique_language.append(k)
    # print(unique_language)
    for i in director_movie:
        if i not in unique_director:
            for k in i:
                if k not in unique_director:
                    unique_director.append(k)
    # print(unique_director)
    for i in language_movie:
        for k in i:
            if k not in unique_language:
                unique_language.append(k)
    new_dict2={}
    for director in unique_director:
        for details in soup:
            for detail in details["director"]:
                if director==detail:
                    # print(director)
                    new_dict={}
                    for j in unique_language:
                        count=1
                        for m in language_movie:
                            if j==m:
                                count=count+1
                        new_dict[j]=count
                    print(new_dict)
                    new_dict2[detail]=new_dict 
    pprint(new_dict2)   
    data=open("saraltask10.json","w")
    saral=json.dumps(new_dict2, indent=4)
    data.write(saral)
    pprint(new_dict)
analyse_language_and_directors(scrape_movie_details())