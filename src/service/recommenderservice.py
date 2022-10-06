import pandas as pd
from src.service.solrservice import search_film_by_id as dbservice,search_film_by_ids as dbSammlungservice

def recommend_for_movie(movie_id):
    """This method returns movies including information as a recommendation for one movie."""
    neighbors = get_neighbors(movie_id)
    movie_information_self = get_movie_information_self(neighbors[0])
    movie_information_neighbors = get_movie_information_neighbors(neighbors[1:7])
    movie_information_self["recommendations"] = movie_information_neighbors
    return movie_information_self

def recommend_for_movies(movie_ids):
    """This method returns movies including information as multiple recommendations for multiple movies."""
    gesamtRecommendation = []
    for i in movie_ids:
        gesamtRecommendation.append(recommend_for_movie(int(i)))
    return gesamtRecommendation

def recommend_for_movie_list(movie_ids):
    """This method returns movies including information as a shared recommendation for multiple movies."""
    movie_ids_ints = list(map(int, movie_ids))
    shared_neighbors = get_shared_neighbors_for_list(movie_ids_ints)
    movie_information_neighbors = get_movie_information_neighbors(shared_neighbors)
    return movie_information_neighbors

def get_neighbors(movie_id):
    """This method calculates a list of movieids as a recommendation for one input movie."""
    df = pd.read_csv('neighbours_ids.csv')
    neighbors = df.iloc[movie_id-1]
    if(neighbors[0]!=movie_id):
        print('Error in "src.service.recommenderservice.recommend_for_movie" - First Element is not the requested movie')
    else:
        neighbors = neighbors.tolist()
        return neighbors

def get_shared_neighbors_for_list(movie_ids):
    """This method calculates a list of movieids as a shared recommendation for multiple movies."""
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

def get_movie_information_neighbors(neighbors):
    """This method returns information from the DB for multiple movies."""
    result = dbSammlungservice(neighbors)
    return result

def get_movie_information_self(self_id):
    """This method returns information from the DB for one movie."""
    movie_information = dbservice(self_id)
    if movie_information:
        return movie_information