from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json


# .............................................Task1............................................................
data=open("saraltask1.json")
task=json.load(data)
# pprint(task)

#...............................................task2.............................................................
def group_by_year(name):
    year=[]
    unique_year=[]
    new_list=[]
    for divs in name:
        years=divs["movie_year"]
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
group_by_year(task)



# #.................................................task3.........................................................
# def scrape_top_list(task):
#     dict_new={"1960":[], "1970":[],"1980":[],"1990":[],"2000":[],"2010":[],"2020":[]}
#     for i in task:
#         if i["movie_year"]>=1960 and i["movie_year"]<=1969:
#             dict_new["1960"].append(i)
#         elif i["movie_year"]>=1970 and i["movie_year"]<=1979:
#             dict_new["1970"].append(i)
#         elif i["movie_year"]>=1980 and i["movie_year"]<=1989:
#             dict_new["1980"].append(i)
#         elif i["movie_year"]>=1990 and i["movie_year"]<=1999:
#             dict_new["1990"].append(i)
#         elif i["movie_year"]>=2000 and i["movie_year"]<=2010:
#             dict_new["2000"].append(i)
#         elif i["movie_year"]>=2010 and i["movie_year"]<=2019:
#             dict_new["2010"].append(i)
#         elif i["movie_year"]>=2020 and i["movie_year"]<=2030:
#             dict_new["2020"].append(i)
#     pprint(dict_new)
# scrape_top_list(task)