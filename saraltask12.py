from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
data=open("saraltask1.json")
task=json.load(data)
def movie_caste_url(soup):
    # soup=soups[:10]
    actor_imbd_list=[]
    for i in soup:
        actor_new_list=[]
        Actor_list=[]
        imbd_list=[]
        url1=i["movie_link"]
        data1= requests.get(url1)
        soup1=BeautifulSoup(data1.text, "html.parser")
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
            actor_imbd_list.append(actor_new_list)
    data=open("saraltask12.json","w")
    saral=json.dumps(actor_imbd_list, indent=4)
    data.write(saral)
    pprint(actor_imbd_list)
movie_caste_url(task)