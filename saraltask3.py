from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
data= requests.get(url)
name=BeautifulSoup(data.text, "html.parser")
def scrape_top_list(task):
    dict_new={"1960":[], "1970":[],"1980":[],"1990":[],"2000":[],"2010":[],"2020":[]}
    for i in task:
        if i["movie_year"]>=1960 and i["movie_year"]<=1969:
            dict_new["1960"].append(i)
        elif i["movie_year"]>=1970 and i["movie_year"]<=1979:
            dict_new["1970"].append(i)
        elif i["movie_year"]>=1980 and i["movie_year"]<=1989:
            dict_new["1980"].append(i)
        elif i["movie_year"]>=1990 and i["movie_year"]<=1999:
            dict_new["1990"].append(i)
        elif i["movie_year"]>=2000 and i["movie_year"]<=2010:
            dict_new["2000"].append(i)
        elif i["movie_year"]>=2010 and i["movie_year"]<=2019:
            dict_new["2010"].append(i)
        elif i["movie_year"]>=2020 and i["movie_year"]<=2030:
            dict_new["2020"].append(i)
    pprint(dict_new)
    data=open("saraltask3.json","w")
    saral=json.dumps(dict_new, indent=4)
    data.write(saral)
    pprint(dict_new)
scrape_top_list(movie_function(name))