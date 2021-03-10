from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
import random
import time
data=open("saraltask1.json")
task=json.load(data)
def scrape_movie_details(soup):
    list_movie=[]
    for i in soup:
        url1=i["movie_link"]
        data1= requests.get(url1)
        soup1=BeautifulSoup(data1.text, "html.parser")
        detail_movie={}
        list_director=[]
        list_language=[]
        actor_new_list=[]
        Actor_list=[]
        imbd_list=[]
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
        actor =soup1.find("table", class_="cast_list")
        for ac in actor.find_all("td", class_=""):
            Actor_list.append(ac.text.strip())
            ids=ac.find("a").get("href")
            imbd_id=ids[6:15]
            imbd_list.append(imbd_id)
        for i in range(len(Actor_list)):
            actor_dict={}
            actor_dict["imbd_id"]=imbd_list[i]
            actor_dict["Actor name"]=Actor_list[i]
            actor_new_list.append(actor_dict)
        detail_movie["Cast"]=actor_new_list
    data=open("saraltask4.json","w")
    saral=json.dumps(list_movie, indent=4)
    data.write(saral)
    return list_movie
print(scrape_movie_details(task))