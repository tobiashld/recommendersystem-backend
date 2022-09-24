import pandas as pd
from src.service.solrservice import search_film_by_id as dbservice
#from src.model.movie import movie

def recommend_for_movie(movie_id):
    neighbors = get_neighbors(movie_id)
    movie_information_self = get_movie_information_self(neighbors['self'])
    movie_information_neighbors = get_movie_information_neighbors(neighbors[1:])
    print("self:")
    print(movie_information_self)
    print("neighbors:")
    print(movie_information_neighbors)

def get_neighbors(movie_id):
    df = pd.read_csv('neighbours_ids.csv', names = ['self', 'n_1','n_2','n_3','n_4','n_5','n_6','n_7','n_8','n_9','n_10'])
    neighbors = df.iloc[movie_id-1]
    if(neighbors['self']!=movie_id):
        print('Error in "recommend_for_movie" - First Element is not the requested movie')
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


recommend_for_movie(3)