from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
name=BeautifulSoup(data.text, "html.parser")
def group_by_year(task):
    year=[]
    unique_year=[]
    new_list=[]
    for divs in name.find_all("span", class_='secondaryInfo'):
        years=int(divs.text[1:5])
        year.append(years)
    for i in year:
        if i not in unique_year:
            unique_year.append(i)
    uniques_year=sorted(unique_year)
    print(uniques_year)
    newlist=[]
    for i in uniques_year:
        newdict={}
        for j in task:
            if j["movie_year"]==i:
                newdict[i]=j
                newlist.append(newdict)
    pprint(newlist)
    data=open("saraltask2.json","w")
    saral=json.dumps(newlist, indent=4)
    data.write(saral)
group_by_year(movie_function(name))