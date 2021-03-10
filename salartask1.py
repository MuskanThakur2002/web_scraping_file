from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
soup=BeautifulSoup(data.text, "html.parser")
soup1=soup.prettify()
# print(soup1.text)
data=open("all_data.json","w")
url1=json.dumps(soup1)
data.write(url1)
def movie_function(soup):
    year=[]
    movie_name=[]
    rank=[]
    link=[]
    list_all_data=[]
    for divs in soup.find_all("span", class_='secondaryInfo'):
        years=int(divs.text[1:5])
        year.append(years)
    for name in soup.find_all("td", class_="titleColumn"):
        for names in name.find("a"):
            movie_name.append(names)
    for m in soup.find_all("strong"):
        rank.append(m.text)
    for links in soup.find_all("td", class_="titleColumn"):
        link1=links.a["href"]
        link2="https://www.imdb.com"+link1
        link.append(link2)
    i=0
    while i<250:
        all_data={}
        all_data["serial no"]=i+1
        all_data["movie_name"]=movie_name[i]
        all_data["movie_year"]=year[i]
        all_data["movie_rank"]=rank[i]
        all_data["movie_link"]=link[i]
        list_all_data.append(all_data)
        i=i+1
    data=open("saraltask1.json","w")
    saral=json.dumps(list_all_data, indent=4)
    data.write(saral)
    return list_all_data
# pprint(movie_function(soup))