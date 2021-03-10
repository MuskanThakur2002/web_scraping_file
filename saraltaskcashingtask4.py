# from salartask1 import movie_function
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
# ...........................................Task4,5..........................................................
# data=open("saraltask1.json")
# task=json.load(data)
def scrape_movie_details():
    data=open("saraltaskch4.json")
    saral=json.load(data)
    return saral
# pprint(scrape_movie_details())

# # # ...................................................Task6..................................................

def analyse_movies_language(soup):
    language_movie=[]
    unique_language=[]
    for lan in soup:
        language_movie.append(lan["movie_language"])
    # print(language_movie)
    for i in language_movie:
            for k in i:
                if k not in unique_language:
                    unique_language.append(k)
    # print(unique_language)
    new_dict={}
    for i in unique_language:
        count=1
        for j in language_movie:
            for k in j:
                if i == k:
                    count=count+1
            new_dict[i]=count
    data=open("saraltask6.json","w")
    saral=json.dumps(new_dict, indent=4)
    data.write(saral)
    print(new_dict)
analyse_movies_language(scrape_movie_details())
# # ...........................................task7............................................................

# def director_analysis(soup):
#     director_movie=[]
#     unique_director=[]
#     for lan in soup:
#         director_movie.append(lan["director"])
#     # print(director_movie)
#     for i in director_movie:
#         if i not in unique_director:
#             for k in i:
#                 if k not in unique_director:
#                     unique_director.append(k)
#     # print(unique_director)
#     new_dict={}
#     for i in unique_director:
#         count=1
#         for j in director_movie:
#             for k in j:
#                 if i == k:
#                     count=count+1
#         new_dict[i]=count
#     data=open("saraltask7.json","w")
#     saral=json.dumps(new_dict, indent=4)
#     data.write(saral)
#     pprint(new_dict)
# director_analysis(scrape_movie_details())

#....................................................Task10....................................................
# def analyse_language_and_directors(soup):
#     director_movie=[]
#     unique_director=[]
#     language_movie=[]
#     unique_language=[]
#     for lan in soup:
#         director_movie.append(lan["director"])
#         language_movie.append(lan["movie_language"])
#     # print(language_movie)
#     for i in language_movie:
#         for k in i:
#             if k not in unique_language:
#                 unique_language.append(k)
#     # print(unique_language)
#     for i in director_movie:
#         if i not in unique_director:
#             for k in i:
#                 if k not in unique_director:
#                     unique_director.append(k)
#     for i in language_movie:
#         for k in i:
#             if k not in unique_language:
#                 unique_language.append(k)
#     new_dict2={}
#     for director in unique_director:
#         for details in soup:
#             for detail in details["director"]:
#                 if director==detail:
#                     new_dict={}
#                     for j in unique_language:
#                         # print(j)
#                         count=1
#                         for m in language_movie:
#                             for k in m:
#                                 if j==k:
#                                     count=count+1
#                                 new_dict[j]=count
#                     new_dict2[detail]=new_dict   
#     data=open("saraltask10.json","w")
#     saral=json.dumps(new_dict2, indent=4)
#     data.write(saral)
#     pprint(new_dict2)
# analyse_language_and_directors(scrape_movie_details())

# .................................................Task11.....................................................

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
director_analysis(scrape_movie_details())