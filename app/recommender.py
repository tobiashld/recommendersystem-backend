import pandas as pd
from src.service.solrservice import search_film_by_id as dbservice
from src.model.movie import movie

def recommend_for_movie(movie_id):
    df = pd.read_csv('neighbours_ids.csv', names = ['self', 'n_1','n_2','n_3','n_4','n_5','n_6','n_7','n_8','n_9','n_10'])
    neighbors = df.iloc[movie_id-1]
    if(neighbors['self']!=movie_id):
        print('Error in "recommend_for_movie" - First Element is not the requested movie')
    else:
        #neighbors = neighbors.drop(['self'])
        #neighbors = neighbors.tolist()
        get_movie_information(neighbors)
    return neighbors

def get_movie_information(neighbors):
    for i in neighbors:
        print(i)
        print(dbservice(i))
    return True

#recommendations = 
recommend_for_movie(1)

#print(recommendations)