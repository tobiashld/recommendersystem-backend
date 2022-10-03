import pandas as pd
import json
from src.service.solrservice import search_film_by_id as dbservice,search_film_by_ids as dbSammlungservice

def recommend_for_movies(movie_ids):
    gesamtRecommendation = []
    for i in movie_ids:
        gesamtRecommendation.append(recommend_for_movie(int(i)))
    return gesamtRecommendation

def recommend_for_movie(movie_id):
    neighbors = get_neighbors(movie_id)
    movie_information_self = get_movie_information_self(neighbors[0])
    movie_information_neighbors = get_movie_information_neighbors(neighbors[1:])
    
    movie_information_self["recommendations"] = movie_information_neighbors
    return movie_information_self

def recommend_for_movie_list(movie_ids):
    movie_ids_ints = list(map(int, movie_ids))
    shared_neighbors = get_shared_neighbors_for_list(movie_ids_ints)
    movie_information_neighbors = get_movie_information_neighbors(shared_neighbors)
    return movie_information_neighbors

def get_shared_neighbors_for_list(movie_ids):
    shared_neighbors = []
    if(len(movie_ids)==1):
        neighbors = get_neighbors(movie_ids[0])
        shared_neighbors = neighbors[1:7]
    # The first 3 neighbours of each movie from the request are taken as shared neighbours.
    # If these are already part of the request or the shared neighbors list, the next neighbour of the current movie is jumped to, and so on.
    # If in this way for a movie under 3 neighbors are determined, then it contributes under 3 recommendations to the total recommendation
    else:
        for i in movie_ids:
            neighbors = get_neighbors(i)
            rec_counter = 0
            for j in neighbors:
                if(not j in shared_neighbors and not j in movie_ids and rec_counter < 3):
                    shared_neighbors.append(j)
                    rec_counter +=1
    return shared_neighbors

def get_neighbors(movie_id):
    df = pd.read_csv('neighbours_ids.csv', names = ['self', 'n_1','n_2','n_3','n_4','n_5','n_6','n_7','n_8','n_9','n_10'])
    neighbors = df.iloc[movie_id-1]
    if(neighbors['self']!=movie_id):
        print('Error in "src.service.recommenderservice.recommend_for_movie" - First Element is not the requested movie')
    else:
        neighbors = neighbors.tolist()
        return neighbors

def get_movie_information_neighbors(neighbors):
    result = dbSammlungservice(neighbors)
    return result

def get_movie_information_self(self_id):
    movie_information = dbservice(self_id)
    if movie_information:
        return movie_information

#print(get_shared_neighbours_for_list([1,2,3]))
# Justice League Dinger
#print(get_shared_neighbors_for_list([2654,7667,12601,13370]))
#print(get_shared_neighbors_for_list([1]))

#recommend_for_movie_list([2654,7667,12601,13370])