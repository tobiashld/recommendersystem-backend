import pandas as pd
import json
from src.service.solrservice import search_film_by_id as dbservice

def recommend_for_movies(movie_ids):
    gesamtRecommendation = []
    for i in movie_ids:
        gesamtRecommendation.append(recommend_for_movie(int(i)))
    return gesamtRecommendation

def recommend_for_movie(movie_id):
    neighbors = get_neighbors(movie_id)
    movie_information_self = get_movie_information_self(neighbors['self'])
    movie_information_neighbors = get_movie_information_neighbors(neighbors[1:])

    #print(json_neighbors)
    #print("self:")
    #print(json_self)
    #print("neighbors:")
    #print(json_neighbors)   
    movie_information_self["recommendations"] = movie_information_neighbors
    return movie_information_self

def get_neighbors(movie_id):
    df = pd.read_csv('neighbours_ids.csv', names = ['self', 'n_1','n_2','n_3','n_4','n_5','n_6','n_7','n_8','n_9','n_10'])
    neighbors = df.iloc[movie_id-1]
    if(neighbors['self']!=movie_id):
        print('Error in "src.service.recommenderservice.recommend_for_movie" - First Element is not the requested movie')
    else:        
        #neighbors = neighbors.drop(['self'])
        #neighbors = neighbors.tolist()
        return neighbors

def get_movie_information_neighbors(neighbors):
    result = []
    for i in neighbors:
       movie_information = dbservice(i)
       if(movie_information):
            result.append(movie_information)
    return result

def get_movie_information_self(self_id):
    movie_information = dbservice(self_id)
    if(movie_information):
        return movie_information

#recommend_for_movie(3)
#recommend_for_movies([1,3])
