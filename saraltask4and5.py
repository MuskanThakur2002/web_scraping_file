from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
import random
import time
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
name=BeautifulSoup(data.text, "html.parser")
def scrape_movie_details(soups):
    list_movie=[]
    for i in soup:
        time.sleep(random_sleep)
        url1=i["movie_link"]
        data1= requests.get(url1)
        soup1=BeautifulSoup(data1.text, "html.parser")
        detail_movie={}
        list_director=[]
        list_language=[]
        detail_movie["movie_name"]=i["movie_name"]
        names =soup1.find("div", class_="credit_summary_item")
        for name in names.find_all("a"):
            list_director.append(name.text)
        detail_movie["director"]=list_director
        for man in soup1.find_all("div", class_="txt-block"):
            for mans in man("a"):
                j=mans.get("href")
                if j=="/search/title?country_of_origin=in" :
                    detail_movie["movie_country"]=mans.text
                elif "/search/title?title_type=feature&primary_language" in j:
                    list_language.append(mans.text)
                    detail_movie["movie_language"]=list_language
            for runtime in man.find_all("time"):
                detail_movie["runtime"]=runtime.text
        poster=soup1.find("div", class_="poster")
        for links in poster.find_all("img"):
            link=links.get("src")
            detail_movie["poster_img_url"]=link
        for genres in soup1.find_all("div", class_="see-more inline canwrap"):
            genres_movie=genres.find("a")
            detail_movie["genres"]=genres_movie.text
        list_movie.append(detail_movie)
    data=open("saraltaskch4.json","w")
    saral=json.dumps(list_movie, indent=4)
    data.write(saral)
    return list_movie
print(scrape_movie_details(movie_function(name)))